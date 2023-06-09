import pytest
import server
from server import app
import socket
import subprocess


# import os


# @pytest.fixture
# def client():
#     """this is the fixture that sets a client for the tests"""
#     server.app.testing = True
#     with server.app.test_client() as client:
#         yield client


@pytest.fixture(autouse=True)
def clubs_fixture():
    """This is the fixture that sets a fake list of clubs for the tests."""
    clubs = {
        "clubs": [
            {"name": "club_1", "email": "club_1@cluba.com", "points": 20},
            {"name": "club_2", "email": "club_2@clubb.com", "points": 20},
            {"name": "club_3", "email": "club_3@clubc.com", "points": 20}
        ]
    }
    return clubs


@pytest.fixture(scope="session")
def flask_port():
    ## Ask OS for a free port.
    #
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        addr = s.getsockname()
        port = addr[1]
        return port


#
@pytest.fixture(autouse=True)
def LiveServerTestCase(flask_port):
    live_server = subprocess.Popen(['flask', '--app', 'server', 'run', '--port', str(flask_port)])
    try:
        yield live_server
    finally:
        live_server.terminate()
