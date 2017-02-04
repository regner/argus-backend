#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

from .models import CharacterNameModel
from .base import BaseService
from ..extensions import db


class CharacterNameService(BaseService):
    __model__ = CharacterNameModel
    __db__ = db

    def create(self, character_id, character_name):
        new_model = self.__model__(character_id, character_name)
        self.save(new_model)

        return new_model

    def update(self, model, new_name):
        self._isinstance(model)

        model.character_name = new_name
        model.last_updated = datetime
        self.save(model)

        return model

    def update_or_create(self, character_id, character_name):
        name = self.get(character_id)

        if name is None:
            name = self.create(character_id, character_name)

        if name.name != character_name:
            name = self.update(name, character_name)

        return name


character_name_service = CharacterNameService()
