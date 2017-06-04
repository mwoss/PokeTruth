import requests
from truthmeas.data.pokemons import poke_list
import simplejson
from truthmeas.pokemon import Pokemon

BASE_URL = 'http://pokeapi.co/api/v1'
CHOICE = ['pokemon']
CLASSES = {'pokemon': Pokemon, }


def get(**kwargs):
    if list(kwargs.keys())[0] in CHOICE:
        return make_request(kwargs)
    else:
        raise ValueError


def _request(url):
    req = requests.get(url)
    if req.status_code == 200:
        return _to_json(req.text)
    else:
        raise ConnectionError


def _to_json(request):
    try:
        data = simplejson.loads(request)
        return data
    except simplejson.JSONDecodeError:
        raise simplejson.JSONDecodeError('Json error')


def _get_poke_id(name):
    proper_input = name.capitalize()
    return poke_list.index(proper_input);


def _get_poke_url(input_map):
    map_key = list(input_map.keys())[0]
    map_value = list(input_map.values())[0]

    poke_id = _get_poke_id(str(map_value)) + 1
    return "/".join([BASE_URL, str(map_key), str(poke_id), ''])


def make_request(input_map):
    f_url = _get_poke_url(input_map)
    data = _request(f_url)
    choice = CLASSES[list(input_map.keys())[0]]
    return choice(data)
