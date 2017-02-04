#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from api.extensions import db


class LinkedCharacterModel(db.Model):
    __tablename__ = 'linked_characters'

    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character_names.id'), nullable=False)
    character_name = db.relationship('CharacterNameModel')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
