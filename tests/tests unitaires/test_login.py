import server


class TestLogin:
    def test_correct_email_should_return_200_status_code(self, client, clubs_fixture, mocker):
        mocker.patch.object(server, 'clubs', clubs_fixture['clubs'])
        email = clubs_fixture['clubs'][0]['email']
        data = {'email': email}
        response = client.post('/showSummary', data=data)

        assert response.status_code == 200

    def test_wrong_email_should_return_200_status_code(self, client, clubs_fixture, mocker):
        mocker.patch.object(server, 'clubs', clubs_fixture['clubs'])
        email = 'fake@fake.com'
        data = {'email': email}
        response = client.post('/showSummary', data=data)

        assert b"<li>unknown email, try again</li>" in response.data