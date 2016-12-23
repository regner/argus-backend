#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ...utils import generate_request_url, build_oauth_client

from flask import current_app
from flask_restful import Resource


class Redirect(Resource):
    def get(self):
        provider_config = current_app.config['OAUTH_EVE']
        client = build_oauth_client(provider_config)
        url = generate_request_url(client, provider_config)

        return {'url': url}, 200
