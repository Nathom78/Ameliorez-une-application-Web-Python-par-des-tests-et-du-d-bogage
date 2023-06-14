from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from server import clubs, competitions


# competition_3 = str(competitions[2]["name"]).replace(" ", "%20")
def str_url():
    competition_3 = str(competitions[2]["name"]).replace(" ", "%20")
    print(competitions[2]["name"])
    return competition_3


class TestFinal:
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
        print(f"capture d'écran sauvegardé : {self.driver.get_screenshot_as_file('Screenshots/Get_board.png')}")
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
        # Identification
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

        # page Welcome

        assert "Summary | GUDLFT Registration" in self.driver.title

    def test_purchase_route(self, flask_port):

        print(f"capture d'écran sauvegardé : {self.driver.get_screenshot_as_file('Screenshots/before_booking.png')}")

        # test past competition
        competition_1 = competitions[0]["name"]
        print(competition_1)
        festival_1 = self.driver.find_element(By.PARTIAL_LINK_TEXT, competition_1)
        festival_1.click()
        message = self.driver.find_element(By.CLASS_NAME, "class")
        print(message)
        expected_value = "sorry, this competition already took place"
        assert expected_value in message

        # test future competition
        competition_3 = str_url()

        print(competition_3)
        competition_3_points = competitions[2]["numberOfPlaces"]
        print(competition_3_points)
        festival_3 = self.driver.find_element(By.PARTIAL_LINK_TEXT, competition_3)
        festival_3.click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_located_to_be_selected((By.NAME, "places")))
        print(element)
        element.clear()
        element.send_key(13)
        logout = self.driver.find_element(By.LINK_TEXT, "Logout")
        logout.click()
        assert "GUDLFT Registration" in self.driver.title
