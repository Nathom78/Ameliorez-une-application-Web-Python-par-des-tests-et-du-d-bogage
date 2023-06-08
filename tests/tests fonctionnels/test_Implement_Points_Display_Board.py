# When:
#
# A secretary logs into the app
#
# Then:
#
# They should be able to see the list of clubs and their associated current points balance.

import server
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

HOSTNAME = "http://127.0.0.1:+5000/"


def live_server():
    # env = os.environ.copy()
    # env["FLASK_APP"] = "server"
    live_server = subprocess.Popen(['flask', '--app', 'server', 'run', '--port', str(4099)])
    try:
        yield live_server
    finally:
        live_server.terminate()


class TestBoard:

    def setUp(self):
        # self.driver = webdriver.Chrome()
        # self.driver = webdriver.Safari()
        # self.driver = webdriver.ChromiumEdge()
        self.driver = webdriver.Edge()

    # def test_server_is_up_and_running(self):
    #     http = urllib3.PoolManager()
    #     response = http.request("GET", self.get_server_url())
    #     print(self.get_server_url())
    #     self.assertEqual(response.status, 200)
    # def test_request(self, live_server, flask_port):
    #     response = server.app.get(f"http://localhost:{flask_port}")
    #     assert response. == 200

    def test_displaying_points_board(self, clubs_fixture, mocker):
        self.driver = webdriver.Edge()
        # ouvrir le client test
        mocker.patch.object(server, "clubs", clubs_fixture["clubs"])

        club = clubs_fixture["clubs"][0]
        # club_email = club["email"]
        club_email = "john@simplylift.co"
        live_server()
        # Ouvrir le navigateur avec le webdriver
        driver = self.driver
        # Identification
        driver.get(f"http://localhost:4099")
        email = driver.find_element(By.NAME, "email")
        email.clear()
        email.send_keys(club_email)
        email.send_keys(Keys.RETURN)
        # Cliquer sur le bouton point_board
        # assert "Summary | GUDLFT Registration" in driver.title
        driver.find_element(By.ID, "button_board").click()

        assert "Points board" in driver.title
        driver.close()
