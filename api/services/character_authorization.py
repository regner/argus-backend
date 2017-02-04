#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .models import CharacterAuthModel
from .base import BaseService
from ..extensions import db


class CharacterAuthorizationService(BaseService):
    __model__ = CharacterAuthModel
    __db__ = db

    def create(self, authorization, refresh, user_id=None, linked_character=None):
        new_model = self.__model__(authorization, refresh, user_id, linked_character)
        self.save(new_model)

        return new_model

    def update(self, model, new_authorization, new_refresh):
        self._isinstance(model)

        model.authorization = new_authorization
        model.refresh = new_refresh
        self.save(model)

        return model


character_authorization_service = CharacterAuthorizationService()
