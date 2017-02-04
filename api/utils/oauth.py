#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

from flask import current_app
from base64 import b64encode
from requests_oauthlib import OAuth2Session
from typing import Tuple, Dict
from flask_restful import abort


def get_basic_oauth_client(token: dict = None):
    """Builds a OAuth2Session."""
    client = OAuth2Session(
        client_id=current_app.config['OAUTH']['CLIENT_ID'],
        scope=current_app.config['OAUTH']['SCOPES'],
        redirect_uri=current_app.config['OAUTH']['URL_REDIRECT'],
    )

    if token is not None:
        client.token = token

    return client


def verify_code(code: str) -> Tuple[Dict, Dict]:
    """Takes the code from an OAuth2 redirect and converts it to a auth token and character details."""
    token_response = convert_code_to_auth_token(code)
    client = get_basic_oauth_client(token=token_response)
    verify_response = client.get(current_app.config['OAUTH']['URL_VERIFY'])

    if verify_response.status_code != requests.codes.ok:
        abort(503, message='Something went wrong with EVE SSO requests')

    return token_response, verify_response.json()


def get_authed_oauth_client():
    return OAuth2Session


def generate_request_url():
    """Uses the WebApplicationClient to generate a URL for users logging in."""
    client = get_basic_oauth_client()
    url, state = client.authorization_url(current_app.config['OAUTH']['URL_AUTH'])

    return url


def build_get_token_auth_header():
    """Combines and base64 encodes the client ID and client secret."""
    combined = '{}:{}'.format(current_app.config['OAUTH']['CLIENT_ID'], current_app.config['OAUTH']['CLIENT_SECRET'])
    result = b64encode(bytes(combined, 'utf-8')).decode('utf-8')
    return result


def convert_code_to_auth_token(code: str):
    """Takes an OAuth2 code and converts it to an authorization token."""
    client = get_basic_oauth_client()
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic {}'.format(build_get_token_auth_header()),
    }

    return client.fetch_token(
        token_url=current_app.config['OAUTH']['URL_TOKEN'],
        code=code,
        headers=headers
    )
