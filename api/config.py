#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


class AppConfig(object):
    """Config object for the app that pulls from the environment."""
    DEBUG = True
    SECRET_JWT = os.environ.get('SECRET_JWT', 'SomethingReallyComplicated!!!!')
    CACHE_DEFAULT_TIMEOUT = os.environ.get('CACHE_DEFAULT_TIMEOUT', 600)
    CACHE_TYPE = os.environ.get('CACHE_TYPE', 'simple')
    OAUTH_EVE = {
        'CLIENT_ID': 'a72a32f2d4cc41c882132579271ca585',
        'CLIENT_SECRET': '8GNdJtk8sWdzQflrNQdEx2pYrZCK5Kux4WhEwftA',
        'URL_REDIRECT': 'http://localhost:8000/callback',
        'URL_AUTH': 'https://login.eveonline.com/oauth/authorize',
        'URL_TOKEN': 'https://login.eveonline.com/oauth/token',
        'TOKEN_METHOD': 'POST',
        'SCOPES': [
            'esi-planets.manage_planets.v1',
            'esi-assets.read_assets.v1',
            'esi-calendar.read_calendar_events.v1',
            'esi-bookmarks.read_character_bookmarks.v1',
            'esi-wallet.read_character_wallet.v1',
            'esi-characters.read_contacts.v1',
            'esi-corporations.read_corporation_membership.v1',
            'esi-killmails.read_killmails.v1',
            'esi-location.read_location.v1',
            'esi-location.read_ship_type.v1',
            'esi-skills.read_skillqueue.v1',
            'esi-skills.read_skills.v1',
            'esi-universe.read_structures.v1',
        ],
    }
