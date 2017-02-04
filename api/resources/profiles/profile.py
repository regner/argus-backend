#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ...services import user_service
from ...utils.decorators import require_auth

from flask import request
from flask_restful import Resource


class Profile(Resource):
    @require_auth()
    def get(self):
        user = user_service.get(request.jwt['user_id'])

        return {
            'id': user.id,
            'character': {
                'id': user.character_id,
                'name': user.character_name.name
            },
            'linked_characters': user.linked_characters,
        }
