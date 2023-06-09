import pytest

import server


@pytest.fixture
def client():
<<<<<<< HEAD
    """this is the fixture that sets a client for the tests"""
=======
    """this is the fixture that sets a client for the tests."""
>>>>>>> origin/BUG/Clubs_should_not_be_able_to_use_more_than_their_points_allowed_#2
    server.app.testing = True
    with server.app.test_client() as client:
        yield client


@pytest.fixture
def clubs_fixture():
    """This is the fixture that sets a fake list of clubs for the tests."""
    clubs = {'clubs': [{'name': 'club_1', 'email': 'club_1@club_a.com', 'points': 20},
                       {'name': 'club_2', 'email': 'club_2@club_b.com', 'points': 20},
                       {'name': 'club_3', 'email': 'club_3@club_c.com', 'points': 20}
                       ]
             }
    return clubs


@pytest.fixture
def competitions_fixture():
    competitions = {'competitions': [
        {
            "name": "Test compet A",
            "date": "2023-05-25 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Test compet B",
            "date": "2022-10-22 13:30:00",
            "numberOfPlaces": "13"
        }
    ]}
    return competitions
