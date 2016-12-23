#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json


def test_redirect(client):
    """Test we get the correct redirect URL back for the EVE SSO."""
    response = client.get('/api/auth/redirect/')
    json_response = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert json_response == {
        'url': 'https://login.eveonline.com/oauth/authorize?response_type=code&client_id=a72a32f2d4cc41c882132579271ca585&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Fcallback&scope=esi-planets.manage_planets.v1+esi-assets.read_assets.v1+esi-calendar.read_calendar_events.v1+esi-bookmarks.read_character_bookmarks.v1+esi-wallet.read_character_wallet.v1+esi-characters.read_contacts.v1+esi-corporations.read_corporation_membership.v1+esi-killmails.read_killmails.v1+esi-location.read_location.v1+esi-location.read_ship_type.v1+esi-skills.read_skillqueue.v1+esi-skills.read_skills.v1+esi-universe.read_structures.v1'
    }
