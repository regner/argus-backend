#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from api.extensions import db


class CharacterAuthModel(db.Model):
    __tablename__ = 'character_authorizations'

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('UserModel')

    linked_character_id = db.Column(db.Integer, db.ForeignKey('linked_characters.id'))
    linked_character = db.relationship('LinkedCharacterModel')

    authorization = db.Column(db.String, nullable=False)
    refresh = db.Column(db.String, nullable=False)

    def __init__(self, authorization, refresh, user_id=None, linked_character_id=None):
        self.authorization = authorization
        self.refresh = refresh

        if user_id is not None:
            self.user_id=user_id

        elif linked_character_id is not None:
            self.linked_character_id=linked_character_id
