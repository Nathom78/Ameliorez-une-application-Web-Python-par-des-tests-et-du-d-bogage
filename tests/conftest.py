import pytest

import server


@pytest.fixture
def client():
    """this is the fixture that sets a client for the tests"""
    server.app.testing = True
    with server.app.test_client() as client:
        yield client


@pytest.fixture
def clubs_fixture():
    """This is the fixture that sets a fake list of clubs for the tests."""
    clubs = {
        "clubs": [
            {"name": "club_1", "email": "club_1@club_a.com", "points": 20},
            {"name": "club_2", "email": "club_2@club_b.com", "points": 20},
            {"name": "club_3", "email": "club_3@club_c.com", "points": 20}
        ]
    }
    return clubs
