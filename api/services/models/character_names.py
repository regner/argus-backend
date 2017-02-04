#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from api.extensions import db

from datetime import datetime


class CharacterNameModel(db.Model):
    __tablename__ = 'character_names'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    last_updated = db.Column(db.DateTime, nullable=False)

    def __init__(self, character_id, character_name):
        self.id = character_id
        self.name = character_name
        self.last_updated = datetime.now()
