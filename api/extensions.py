#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask_cache import Cache
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
cache = Cache()
migrate = Migrate()


def configure_extensions(app):
    """Registers all relevant extensions."""
    cache.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
