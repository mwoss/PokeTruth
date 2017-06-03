from beckett.clients import BaseClient
from truthmeas.pokeresource import PokemonResource, TypeResource
from truthmeas.request import choice, make_request


def get(**kwargs):
    print(kwargs)
    print(kwargs.keys())
    print(list(kwargs.keys())[0])
    if list(kwargs.keys())[0] in choice:
        print(kwargs)
        return make_request(kwargs)
    else:
        raise ValueError


class PokeClient(BaseClient):
    class Meta(BaseClient.Meta):
        name = 'pokemon_client'
        base_url = 'http://pokeapi.co/api/v1'
        resources = (
            PokemonResource,
            TypeResource
        )
