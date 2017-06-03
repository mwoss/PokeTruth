from truthmeas.request import make_request
from truthmeas.parseclient import PokeClient, get
if __name__ == "__main__":
    # data = {"pokemon": "bulbasaur"}
    # json = make_request(data)
    # print(json)
    client = PokeClient()
    pokemon = get(pokemon='bulbasaur')
    print(pokemon.attack)