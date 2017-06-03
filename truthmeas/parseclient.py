from beckett.clients import BaseClient
from truthmeas.pokeresource import PokemonResource
from truthmeas.request import CHOICE, make_request


def get(**kwargs):
    if list(kwargs.keys())[0] in CHOICE:
        return make_request(kwargs)
    else:
        raise ValueError


class PokeClient(BaseClient):
    class Meta(BaseClient.Meta):
        name = 'pokemon_client'
        base_url = 'http://pokeapi.co/api/v1'
        resources = (
            PokemonResource,
        )
