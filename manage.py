#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask_script import Manager, Server
from flask_migrate import MigrateCommand

from api import create_app

app = create_app()
manager = Manager(app)

manager.add_command("runserver", Server("localhost", port=8000))
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
