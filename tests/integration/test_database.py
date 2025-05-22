import pytest
import json
from app.models.controller import *

def test_database(json_path):
    create_tables()

    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    add_new_users(data['results'])

    assert len(get_all_users()) == 1

    add_new_users(data['results'])

    assert len(get_all_users()) == 2

