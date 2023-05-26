# When:
# A secretary tries to book more than 12 places in one competition
# Then:
# Those places are confirmed
# Expected:
# They should be able to book no more than 12 places.
# The UI should prevent them from booking more than 12 places.
# The places are correctly deducted from the competition.

import server

MESSAGE_4 = b"Sorry, you cannot book more than 12 places."


class TestPurchase:
    def test_book_more_12_places_should_return_error_message(self, client, clubs_fixture, competitions_fixture, mocker):
        """
        This test creates a client, trie to book more than 12 places
        and verifies the status_code, and error message.
        """

        mocker.patch.object(server, "clubs", clubs_fixture["clubs"])
        mocker.patch.object(server, "competitions", competitions_fixture["competitions"])
        club = clubs_fixture["clubs"][0]
        competition = competitions_fixture["competitions"][0]

        data = {"places": 13,
                "club": club["name"],
                "competition": competition["name"]
                }

        response = client.post("/purchasePlaces", data=data)

        assert MESSAGE_4 in response.data
        assert response.status_code == 200

    def test_book_12_places_should_return_error_message(self, client, clubs_fixture, competitions_fixture, mocker):
        """
        This test creates a client, trie to book 12 places
        and verifies the status_code, and error message.
        """

        mocker.patch.object(server, "clubs", clubs_fixture["clubs"])
        mocker.patch.object(server, "competitions", competitions_fixture["competitions"])
        club = clubs_fixture["clubs"][0]
        competition = competitions_fixture["competitions"][0]

        data = {"places": 12,
                "club": club["name"],
                "competition": competition["name"]
                }

        response = client.post("/purchasePlaces", data=data)

        assert MESSAGE_4 not in response.data
        assert response.status_code == 200

    def test_book_less_12_places_should_return_error_message(self, client, clubs_fixture, competitions_fixture, mocker):
        """
            This test creates a client, trie to book less than 12 places
            and verifies the status_code, and error message.
        """

        mocker.patch.object(server, "clubs", clubs_fixture["clubs"])
        mocker.patch.object(server, "competitions", competitions_fixture["competitions"])
        club = clubs_fixture["clubs"][0]
        competition = competitions_fixture["competitions"][0]

        data = {"places": 1,
                "club": club["name"],
                "competition": competition["name"]
                }

        response = client.post("/purchasePlaces", data=data)

        assert MESSAGE_4 not in response.data
        assert response.status_code == 200
