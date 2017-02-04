#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .models import UserModel
from .base import BaseService
from ..extensions import db


class UserService(BaseService):
    __model__ = UserModel
    __db__ = db

    def find_unique_user(self, character_id, owner_hash) -> UserModel:
        """Find a user by char ID and owner hash."""
        return self.__model__.query.filter_by(
            character_id=character_id,
            character_owner_hash=owner_hash
        ).first()

    def create_new_user(self, character_id, owner_hash) -> UserModel:
        new_user = self.__model__(character_id, owner_hash)
        self.save(new_user)

        return new_user

user_service = UserService()
