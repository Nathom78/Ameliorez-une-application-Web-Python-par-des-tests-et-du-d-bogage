import pytest

from server import app


@pytest.fixture
def client():
    app_test = app({"TESTING": True})
    with app_test.test_client() as client:
        yield client


@pytest.fixture
def clubs_fixture():
    clubs = {'clubs': [{'name': 'club_1', 'email': 'club_1@club_a.com', 'points': 20},
                       {'name': 'club_2', 'email': 'club_2@club_b.com', 'points': 20},
                       {'name': 'club_3', 'email': 'club_3@club_c.com', 'points': 20}
                       ]
             }
    return clubs
