#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


class AppConfig(object):
    """Config object for the app that pulls from the environment."""
    DEBUG = True
    JWT_SECRET = os.environ.get('JWT_SECRET', 'SomethingReallyComplicated!!!!')
    JWT_EXPIRY = os.environ.get('JWT_SECRET', 48)
    CACHE_DEFAULT_TIMEOUT = os.environ.get('CACHE_DEFAULT_TIMEOUT', 600)
    CACHE_TYPE = os.environ.get('CACHE_TYPE', 'simple')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'SQLALCHEMY_DATABASE_URI',
        'postgresql://dev:123456@192.168.99.101:32774/argus'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    CELERY_BROKER_URL = 'redis://192.168.99.101:32778/0'
    OAUTH = {
        'CLIENT_ID': 'a72a32f2d4cc41c882132579271ca585',
        'CLIENT_SECRET': '8GNdJtk8sWdzQflrNQdEx2pYrZCK5Kux4WhEwftA',
        'URL_REDIRECT': 'http://localhost:8000/callback',
        'URL_AUTH': 'https://login.eveonline.com/oauth/authorize',
        'URL_TOKEN': 'https://login.eveonline.com/oauth/token',
        'URL_VERIFY': 'https://login.eveonline.com/oauth/verify',
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
