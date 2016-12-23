#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .redirect import Redirect
from .verify import Verify


def configure_resources(api):
    """Configures all resources for the API."""
    api.add_resource(Verify, '/api/auth/verify/')
    api.add_resource(Redirect, '/api/auth/redirect/')
