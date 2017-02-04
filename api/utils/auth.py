#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import jwt

from flask import current_app
from datetime import datetime, timedelta


def build_jwt_token(user_id: int):
    token = {
        'user_id': user_id,
    }

    return encode_token(token)


def encode_token(token: dict):
    token['exp'] = datetime.utcnow() + timedelta(hours=current_app.config['JWT_EXPIRY'])

    return jwt.encode(
        payload=token,
        key=current_app.config['JWT_SECRET'],
    ).decode('UTF-8')


def decode_token(token: dict):
    return jwt.decode(
        jwt=token,
        key=current_app.config['JWT_SECRET'],
    )
