
from truthmeas.poketruth import PokeTruth
if __name__ == "__main__":

    truth = PokeTruth()
    truth.evaluate_sentence('Bulbasaur is not water type pokemon and has 55 attack, he is 20 weight also has 7 height')
    print(truth.sentence_truth)
