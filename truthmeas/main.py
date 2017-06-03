from truthmeas.parseclient import PokeClient, get
if __name__ == "__main__":
    client = PokeClient()
    pokemon = get(pokemon='bulbasaur')
    print(pokemon.weight)