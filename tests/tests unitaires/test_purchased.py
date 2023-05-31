# Given:
#
# A secretary wishes to book a number of places for a competition
#
# When:
#
# They book a number of places on a competition that has happened in the past
# Then:
#
# They receive a confirmation message
# Expected:
#
#  They should not be able to book a place on a post-dated competition (but past competitions should be visible).
# The booking.html page should be displayed for a valid competition.
#
# An error message is displayed when a competition is invalid and a confirmation message is displayed
# when a competition is valid.

import server


class Testpurchase:
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
