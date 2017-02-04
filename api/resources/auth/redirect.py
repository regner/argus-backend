#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ...utils import generate_request_url

from flask_restful import Resource


class Redirect(Resource):
    def get(self):
        url = generate_request_url()

        return {'url': url}, 200
