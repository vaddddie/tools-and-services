import os
import pytest


@pytest.fixture(autouse=True)
def json_path():
    file_path = os.path.normpath(os.path.join(__file__, "../test_json.json")).replace(
        os.sep, "/"
    )
    return file_path