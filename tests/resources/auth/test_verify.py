#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json


def test_verify(client):
    """Test we take an auth token and return 200 if valid."""
    data = {'code': '1234567890'}
    response = client.post('/api/auth/verify/', data=data)
    json_response = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200


def test_verify_fails_validation(client):
    """Test we return a 401 if authoriztion code is invalid."""
    data = {'code': ''}
    response = client.post('/api/auth/verify/', data=data)
    json_response = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 401
