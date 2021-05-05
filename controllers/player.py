''' players controller '''
from werkzeug.exceptions import BadRequest
from templates import players


def index(req):
    return [c for c in players], 200

def show(req, uid):
    return find_by_uid(uid), 200

def create(req):
    new_player = req.get_json()
    new_player['id'] = sorted([c['id'] for c in players])[-1] + 1
    players.append(new_player)
    return new_player, 201

def update(req, uid):
    player = find_by_uid(uid)
    data = req.get_json()
    print(data)
    for key, val in data.items():
        player[key] = val
    return player, 200

def destroy(req, uid):
    player = find_by_uid(uid)
    players.remove(player)
    return player, 204

def find_by_uid(uid):
    try:
        return next(player for player in players if player['id'] == uid)
    except:
        raise BadRequest(f"We don't have that player with id {uid}!")