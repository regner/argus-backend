#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

from .auth import decode_token

from jwt import ExpiredSignatureError, DecodeError
from flask import abort, request


def require_auth():
    def decorator(target):
        @functools.wraps(target)
        def wrapper(*args, **kwargs):
            if 'Authorization' not in request.headers:
                abort(401, 'No Authorization header found.')

            auth_header = request.headers['Authorization']
            garbage, token = auth_header.split(' ')

            try:
                request.jwt = decode_token(token)

            except ExpiredSignatureError:
                abort(401, 'JWT has expired. Please login again.')

            except DecodeError:
                abort(401, 'Error decoding auth token.')

            return target(*args, **kwargs)
        return wrapper
    return decorator
