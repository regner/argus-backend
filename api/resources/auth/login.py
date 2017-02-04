#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask_restful import Resource
from webargs import fields
from webargs.flaskparser import use_args
from ...utils import login_user


class Login(Resource):
    verify_args = {
        'code': fields.Str(required=True),
        'user_id': fields.Str()
    }

    @use_args(verify_args)
    def post(self, args):
        jwt = login_user(args['code'])

        return {
            'jwt': jwt,
        }, 200
