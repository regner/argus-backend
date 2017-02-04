#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from api.extensions import db


class UserModel(db.Model):
    __tablename__ = 'users'
    __table_args__ = (
        db.UniqueConstraint('character_id', 'character_owner_hash', name='_character_owner_uc'),
    )

    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character_names.id'), unique=True, nullable=False)
    character_name = db.relationship('CharacterNameModel')
    character_owner_hash = db.Column(db.String, nullable=False)
    linked_characters = db.relationship('LinkedCharacterModel')
    auth = db.relationship('CharacterAuthModel', uselist=False)

    def __init__(self, character_id, owner_hash):
        self.character_id = character_id
        self.character_owner_hash = owner_hash
