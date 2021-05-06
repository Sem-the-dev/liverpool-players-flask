import json


def test_greeting(api):
    res = api.get('/')
    assert res.status == '200 OK'


def test_get_players(api):
    res = api.get('/players')
    assert res.status == '200 OK'


def test_get_players_by_ID(api):
    res = api.get('/players/1')
    assert res.status == '200 OK'


def test_posts_players(api):
    mock_data = json.dumps({'goals': '3'})
    mock_headers = {'Content-Type': 'application/json'}
    res = api.post('/players/1', data=mock_data, headers=mock_headers)
    assert res.status == '200 OK'


# def test_not_found(self, api):
#     res = api.get('/bob')
#     assert res.status == '404 NOT FOUND'
#     assert 'Oops!' in res.json['message']
