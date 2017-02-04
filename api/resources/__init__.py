#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .auth import configure_resources as cr_auth
from .profiles import configure_resources as cr_profile
from .liveness import Liveness
from .readiness import Readiness


def configure_resources(api):
    """Configures all resources for the API."""
    cr_auth(api)
    cr_profile(api)

    api.add_resource(Liveness, '/liveness/')
    api.add_resource(Readiness, '/readiness/')
