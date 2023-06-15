from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from server import clubs, competitions


def str_url(comp_name, club_name):
    competition_url = f'/book/{str(comp_name).replace(" ", "%20")}/{str(club_name).replace(" ", "%20")}'
    return competition_url


class TestFinal:
    """
    Test fonctionnel with Selenium
    """
    driver = None

    @classmethod
    def setup_class(cls):
        cls.club = clubs[0]
        # Ouvrir le navigateur avec le webdriver approprié
        # driver = webdriver.Chrome()
        cls.driver = webdriver.Edge()
        cls.driver.implicitly_wait(10)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_displaying_points_board_without_login(self, flask_port):
        # Test board route, without connexion
        self.driver.get(f"http://localhost:{flask_port}/board")
        assert "Points board" in self.driver.title
        # test des données affiché
        print(f"capture d'écran sauvegardé : {self.driver.get_screenshot_as_file('static/Get_board.png')}")
        table_td = self.driver.find_elements(By.TAG_NAME, "td")
        text_td = ""
        for element in table_td:
            text_td += element.text
        for club in clubs:
            assert club["name"] in text_td
            print(f"{club['name']} est dans le tableau")
        # test bouton home
        self.driver.find_element(By.ID, "button_id").click()
        url_home = self.driver.current_url
        assert url_home == f"http://localhost:{flask_port}/?"

    def test_login(self, flask_port):
        # Login
        club_email = self.club["email"]
        self.driver.get(f"http://localhost:{flask_port}")

        email = self.driver.find_element(By.NAME, "email")
        button = self.driver.find_element(By.XPATH, "/html/body/form/button")

        email.clear()
        email.send_keys(club_email)

        actions = ActionChains(self.driver)
        actions.move_to_element(button)
        actions.pause(2)
        actions.click(button)
        actions.perform()

        # page Welcome for route showSummary
        assert "Summary | GUDLFT Registration" in self.driver.title

    def test_purchase_route(self, flask_port):
        # template booking for route book with initial point's club.
        print(f"capture d'écran sauvegardé : "
              f"{self.driver.get_screenshot_as_file('static/before_booking.png')}")

        # test past competition
        competition_1 = str_url(competitions[0]["name"], self.club["name"])
        festival_1 = self.driver.find_element(By.XPATH, f'//a[@href="{competition_1}"]')
        festival_1.click()
        message = self.driver.find_element(By.CLASS_NAME, "flashes")
        expected_value = "sorry, this competition already took place"
        assert expected_value in message.text

        # test future competition
        # for more twelve places
        competition_3 = str_url(competitions[2]["name"], self.club["name"])
        competition_3_points = int(competitions[2]["numberOfPlaces"])
        festival_3 = self.driver.find_element(By.XPATH, f'//a[@href="{competition_3}"]')
        festival_3.click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.NAME, "places")))
        element.clear()
        element.send_keys(13)
        element.send_keys(Keys.RETURN)
        message = self.driver.find_element(By.CLASS_NAME, "flashes")
        expected_value = "Sorry, you cannot book more than 12 places."
        assert expected_value in message.text

        # for max point of club, less than twelve
        competition_3_points = 12 if competition_3_points > 12 else competition_3_points
        festival_3 = self.driver.find_element(By.XPATH, f'//a[@href="{competition_3}"]')
        festival_3.click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.NAME, "places")))
        element.clear()
        element.send_keys(competition_3_points)
        element.send_keys(Keys.RETURN)
        message = self.driver.find_element(By.CLASS_NAME, "flashes")
        expected_value = "Great-booking complete!"
        assert expected_value in message.text
        print(f"capture d'écran sauvegardé : "
              f"{self.driver.get_screenshot_as_file('static/after_booking.png')}")

        # Test message in route book\ "Something went wrong-please try again" with bad address.
        self.driver.get(f"http://localhost:{flask_port}/book/Spring%20Festival/SimplLift")
        message = self.driver.find_element(By.CLASS_NAME, "flashes")
        expected_value = "Something went wrong-please try again"
        assert expected_value in message.text

        # Logout
        logout = self.driver.find_element(By.LINK_TEXT, "Logout")
        logout.click()
        assert "GUDLFT Registration" in self.driver.title
