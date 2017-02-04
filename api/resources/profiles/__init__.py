#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .profile import Profile


def configure_resources(api):
    """Configures all resources for the API."""
    api.add_resource(Profile, '/api/profile/')
