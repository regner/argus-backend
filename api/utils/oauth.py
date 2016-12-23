#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from oauthlib.oauth2 import WebApplicationClient


def build_oauth_client(provider_config):
    """Builds a WebApplicationClient with the provided config."""
    return WebApplicationClient(
        client_id=provider_config['CLIENT_ID']
    )


def generate_request_url(client: WebApplicationClient, provider_config):
    """Uses the WebApplicationClient to generate a URL for users logging in."""
    return client.prepare_request_uri(
        uri=provider_config['URL_AUTH'],
        redirect_uri=provider_config['URL_REDIRECT'],
        scope=provider_config['SCOPES']
    )
