#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .auth import build_jwt_token
from .oauth import verify_code
from ..services import user_service, character_authorization_service, character_name_service


def login_user(code: str) -> str:
    auth_token, character_details = verify_code(code)

    character_id = character_details['CharacterID']
    character_name = character_details['CharacterName']
    owner_hash = character_details['CharacterOwnerHash']

    user = user_service.find_unique_user(
        character_id,
        owner_hash
    )

    if user is None:
        create_new_user(
            access_token=auth_token['access_token'],
            refresh_token=auth_token['refresh_token'],
            character_id=character_id,
            character_name=character_name,
            owner_hash=owner_hash
        )

    else:
        character_authorization_service.update(
            model=user.auth,
            new_authorization=auth_token['access_token'],
            new_refresh=auth_token['refresh_token']
        )

    return build_jwt_token(user.id)


def create_new_user(access_token, refresh_token, character_id, character_name, owner_hash):
    character_name_service.update_or_create(character_id, character_name)

    new_user = user_service.create_new_user(
        character_id=character_id,
        character_name=character_name,
        owner_hash=owner_hash,
    )

    character_authorization_service.create(
        authorization=access_token,
        refresh=refresh_token,
        user_id=new_user.id
    )
