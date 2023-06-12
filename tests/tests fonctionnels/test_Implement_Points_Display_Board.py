# When:
#
# A secretary logs into the app
#
# Then:
#
# They should be able to see the list of clubs and their associated current points balance.

from server import clubs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TestBoard:
    def test_displaying_points_board(self, flask_port):
        # chargement des données
        club = clubs[0]
        club_email = club["email"]
        # Ouvrir le navigateur avec le webdriver approprié
        # driver = webdriver.Chrome()
        driver = webdriver.Edge()

        # Identification
        driver.get(f"http://localhost:{flask_port}")
        email = driver.find_element(By.NAME, "email")
        email.clear()
        email.send_keys(club_email)
        email.send_keys(Keys.RETURN)
        # page Welcome
        assert "Summary | GUDLFT Registration" in driver.title
        # Cliquer sur le bouton point_board
        driver.find_element(By.ID, "button_board").click()
        # Affichage de la page board
        assert "Points board" in driver.title
        # test des données affiché
        print(f"capture d'écran sauvegardé : {driver.get_screenshot_as_file('Screenshots/board.png')}")
        table_td = driver.find_elements(By.TAG_NAME, "td")
        text_td = ""
        for element in table_td:
            text_td += element.text
        for club in clubs:
            assert club["name"] in text_td
            print(f"{club['name']} est dans le tableau")

        driver.close()
