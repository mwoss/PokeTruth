import requests
from truthmeas.data.pokemons import poke_list
import simplejson

BASE_URL = 'http://pokeapi.co/api/v1'


def _request(url):
    req = requests.get(url)
    if req.status_code == 200:
        return _to_json(req.text)
    else:
        raise ConnectionError
    pass


def _to_json(request):
    try:
        data = simplejson.loads(request)
        return data
    except simplejson.JSONDecodeError:
        raise simplejson.JSONDecodeError('Json error')
    pass


def _get_poke_id(name):
    proper_input = name.capitalize()
    return poke_list.index(proper_input);


def _get_poke_url(input_map):
    map_key = input_map.keys()[0]
    map_value = input_map.values()[0]

    poke_id = _get_poke_id(str(map_value))

    return "/".join([BASE_URL, str(map_key), poke_id, ''])
