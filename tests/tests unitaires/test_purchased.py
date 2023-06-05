# Given:
#
# A club secretary wishes to redeem points for a place in a competition
#
# When:
#
# The number of places is confirmed
#
# Then:
#
# The amount of club points available remain the same
# Expected:
#
# The amount of points used should be deducted from the club"s balance.

import server


class Testpurchase:
    def test_points_should_be_updated(self, client, clubs_fixture, competitions_fixture, mocker):
        """
        This test creates a client, book places to a competition and verifies the status_code,
        and the new amount of club"s points.
        """
        mocker.patch.object(server, "competitions", competitions_fixture["competitions"])
        mocker.patch.object(server, "clubs", clubs_fixture["clubs"])

        club = clubs_fixture["clubs"][0]
        initial_points = club["points"]

        competition = competitions_fixture["competitions"][0]
        nb_of_places = 4

        data = {
            "club": club["name"],
            "competition": competition["name"],
            "places": nb_of_places
        }
        response = client.post("/purchasePlaces", data=data)

        updated_points = club["points"]
        expected_points = int(initial_points) - nb_of_places

        assert updated_points == expected_points
        assert response.status_code == 200
