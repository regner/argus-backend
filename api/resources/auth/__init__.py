#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .redirect import Redirect
from .login import Login


def configure_resources(api):
    """Configures all resources for the API."""
    api.add_resource(Login, '/api/auth/login/')
    api.add_resource(Redirect, '/api/auth/redirect/')
