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

    def test_book_past_competition_should_return_error_message(self, client, clubs_fixture, past_competitions_fixture,
                                                               mocker):
        """
        This test creates a client, trie to book places to a past competition
        and verifies the status_code, and error message.
        """
        mocker.patch.object(server, "competitions", past_competitions_fixture["competitions"])
        mocker.patch.object(server, "clubs", clubs_fixture["clubs"])

        competition = [comp for comp in past_competitions_fixture["competitions"]
                       if comp["name"] == "Test past compet"][0]
        club = clubs_fixture["clubs"][0]

        data = {"club": club["name"], "competitions": competition["name"]}
        url = f"/book/{competition['name'].replace(' ', '%20')}/{club['name'].replace(' ', '%20')}"
        response = client.post(url, data=data)

        assert response.status_code == 200
        assert b"sorry, this competition already took place" in response.data

    def test_book_future_competition_should_not_return_error_message(self, client, clubs_fixture,
                                                                     past_competitions_fixture, mocker):
        """
        This test creates a client, trie to book places to a future competition
        and verifies the status_code.
        """
        mocker.patch.object(server, "competitions", past_competitions_fixture["competitions"])
        mocker.patch.object(server, "clubs", clubs_fixture["clubs"])
        competition = [comp for comp in past_competitions_fixture["competitions"]
                       if comp["name"] == "Test future compet"][0]

        club = clubs_fixture["clubs"][0]
        data = {"club": club["name"], "competitions": competition["name"]}
        response = client.post(f"/book/{competition['name']}/{club['name']}", data=data)

        assert response.status_code == 200
        assert b"sorry, this competition already took place" not in response.data
