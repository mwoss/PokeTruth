from truthmeas.parseclient import PokeClient, get
from truthmeas.poketruth import PokeTruth
if __name__ == "__main__":
    #client = PokeClient()

    truth = PokeTruth()
    truth.evaluate_sentence('Bulbasaur is not water type pokemon and has 55 attack, he is 20 weight also has 12 height')
    print(truth.pokemon)
    print(truth.argument)
    print(truth.value)
    print(truth.sentence_type)
    pokemon = get(pokemon=truth.pokemon)
    print(pokemon.attack)
    print(getattr(pokemon, 'name'))
    iter = 0
    print(str(iter + 1) + "i s lol")
    print(iter)
    #print(pokemon.male_female_ratio)