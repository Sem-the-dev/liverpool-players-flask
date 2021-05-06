import pytest
import app

@pytest.fixture
def api(monkeypatch):
    # test_players = [
    #     {'id': 1, 'name': 'Test Player 1'},
    #     {'id': 2, 'name': 'Test Player 2'},
    # ]
    # monkeypatch.setattr(app, "players", test_players)

    api = app.app.test_client()
    return api
