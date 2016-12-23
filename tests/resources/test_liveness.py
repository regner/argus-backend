#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json


def test_liveness(client):
    """Test we simply respond with empty 200."""
    response = client.get('/liveness/')
    json_response = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert json_response ==  {}
