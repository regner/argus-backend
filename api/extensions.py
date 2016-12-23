#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask_cache import Cache


cache = Cache()


def configure_extensions(app):
    """Registers all relevant extensions."""
    cache.init_app(app)
