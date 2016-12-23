#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from webargs import fields
from webargs.flaskparser import use_args
from flask_restful import Resource


class Verify(Resource):
    verify_args = {
        'code': fields.Str(required=True)
    }

    @use_args(verify_args)
    def post(self, args):
        if args['code'] != '1234567890':
            return {}, 401

        return {}, 200
