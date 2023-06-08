# When:
#
# A secretary logs into the app
#
# Then:
#
# They should be able to see the list of clubs and their associated current points balance.
import multiprocessing

import urllib3
from flask import Flask
import server
from flask_testing import LiveServerTestCase
from selenium import webdriver
from flask import request, url_for

HOSTNAME = "http://127.0.0.1:5000/"


class TestBoard(LiveServerTestCase):
    def create_app(self):
        server.app.testing = True
        server.app.config.from_object('config')
        # client.config['LIVESERVER_PORT'] = 0
        # Default port is 5000
        server.app.config['LIVESERVER_PORT'] = 8943

        # # Default timeout is 5 seconds
        # client.config['LIVESERVER_TIMEOUT'] = 10

        return server.app

    def setUp(self):
        super().setUp()
        # self.driver = webdriver.Chrome()
        # self.driver = webdriver.Safari()
        # self.driver = webdriver.ChromiumEdge()
        self.driver = webdriver.Edge()

    def test_server_is_up_and_running(self):
        http = urllib3.PoolManager()
        response = http.request("GET", self.get_server_url())
        print(self.get_server_url())
        self.assertEqual(response.status, 200)

    # def test_displaying_points_board(self, clubs_fixture, mocker):
    #     # ouvrir le client test
    #     mocker.patch.object(server, "clubs", clubs_fixture["clubs"])
    #     club = clubs_fixture["clubs"][0]
    #     club_email = club["email"]
    #
    #     # Ouvrir le navigateur avec le webdriver
    #     driver = self.driver
    #     # Identification
    #     driver.get(HOSTNAME)
    #     email = driver.find_element(By.NAME, "email")
    #     email.clear()
    #     email.send_keys(club_email)
    #     email.send_keys(Keys.RETURN)
    #     # Cliquer sur le bouton point_board
    #
    #     driver.find_element(By.ID, "button_board")
    #
    #     assert "Points board" in driver.title

    def tearDown(self):
        self.driver.close()
