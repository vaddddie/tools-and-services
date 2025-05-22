import pytest
import json
import responses
from app.api import get_random_users


class TestAPI:
    def test_api(self, json_path):
        with responses.RequestsMock() as resp:
            with open(json_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            resp.add(
                responses.GET,
                'https://randomuser.me/api/',
                json=data,
                status=200
            )
            
            resp = get_random_users(1)
            with open(json_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                
            assert data['results'][0] == resp[0]