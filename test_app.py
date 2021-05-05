import json

class TESTPLAYERS():
    def test_greeting(self, api):
        res = api.get('/')
        assert res.status == '200 OK'

    def test_get_players(self, api):
        res = api.get('/players')
        assert res.status == '200 OK'
    
    def test_get_players_by_ID(self, api):
        res = api.get('/players/1')
        assert res.status == '200 OK'
        assert res.json['name'] == 'Test Player 1'

    def test_posts_players(self, api):
        mock_data = json.dumps({'name': 'Virgil Van Dijk'})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.post('/players/', data=mock_data, headers=mock_headers)
        assert res.json['id'] == 3

    def test_not_found(self, api):
        res = api.get('/bob')
        assert res.status == '404 NOT FOUND'
        assert 'Oops!' in res.json['message']