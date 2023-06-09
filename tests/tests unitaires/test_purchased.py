# BUG: Clubs should not be able to use more than their points allowed #2
# When:
# A secretary redeems more points than they have available, which would leave them in the negative#
# Then:
# They receive a confirmation message
# Expected:
# They should not be able to redeem more points than available; this should be done within the UI.
# The redeemed points should be correctly deducted from the club"s total.

import server


class TestPurchase:
    def test_more_than_club_points_should_return_error_message(self, client, clubs_fixture, competitions_fixture,
                                                               mocker):
        """
        This test creates a client, trie to book more than the club amount
        of points to a competition and verifies the status_code, and error message.
        """
        mocker.patch.object(server, "clubs", clubs_fixture["clubs"])
        mocker.patch.object(server, "competitions", competitions_fixture["competitions"])
        club = clubs_fixture["clubs"][0]
        competition = competitions_fixture["competitions"][0]

        data = {"places": int(club["points"] + 1),
                "club": club["name"],
                "competition": competition["name"]
                }

        response = client.post("/purchasePlaces", data=data)

        assert b"sorry, you do not have enough points" in response.data
        assert response.status_code == 200

    def test_less_club_points_should_return_no_error_message(self, client, clubs_fixture, competitions_fixture, mocker):
        """
        This test creates a client, trie to book less than the club amount
        of points to a competition and verifies the status_code, and error message.
        """
        mocker.patch.object(server, "clubs", clubs_fixture["clubs"])
        mocker.patch.object(server, "competitions", competitions_fixture["competitions"])
        club = clubs_fixture["clubs"][0]
        competition = competitions_fixture["competitions"][0]

        data = {"places": int(club["points"]),
                "club": club["name"],
                "competition": competition["name"]
                }

        response = client.post("/purchasePlaces", data=data)

        assert b"sorry, you do not have enough points" not in response.data
        assert response.status_code == 200

    def test_equal_club_points_should_return_no_error_message(self, client, clubs_fixture, competitions_fixture,
                                                              mocker):
        """
        This test creates a client, trie to book the club amount
        of points to a competition and verifies the status_code, and no error message.
        """
        mocker.patch.object(server, "clubs", clubs_fixture["clubs"])
        mocker.patch.object(server, "competitions", competitions_fixture["competitions"])
        club = clubs_fixture["clubs"][0]
        competition = competitions_fixture["competitions"][0]

        data = {"places": int(club["points"] - 1),
                "club": club["name"],
                "competition": competition["name"]
                }

        response = client.post("/purchasePlaces", data=data)

        assert b"sorry, you do not have enough points" not in response.data
        assert response.status_code == 200
