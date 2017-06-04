from truthmeas.poketruth import PokeTruth
from truthmeas.customexception import NoPokemonFound, DemoVersionException
import pytest

class TestPokeTrust:
    def test_sentance1(self):
        truth = PokeTruth()
        truth.evaluate_sentence(
            'Bulbasaur is not water type pokemon and has 55 attack, he is 20 weight also has 7 height')
        assert truth.sentence_truth == [True, False, False, True]

    def test_sentence2(self):
        truth = PokeTruth()
        truth.evaluate_sentence(
            'Bulbasaur is grass type pokemon')
        assert truth.pokemon == 'Bulbasaur'

    def test_sentence3(self):
        truth = PokeTruth()
        truth.evaluate_sentence(
            'Bulbasaur is grass type pokemon and has 55 attack')
        assert truth.argument == ['type', 'attack']

    def test_sentence4(self):
        truth = PokeTruth()
        truth.evaluate_sentence(
            'Bulbasaur is grass type pokemon and has 55 attack')
        assert truth.value == ['grass', '55']

    def test_take_value1(self):
        index = 3
        words = ['Bulbasaur', 'is', 'grass', 'type', 'pokemon']
        truth = PokeTruth()
        value = truth._take_value(index, words)
        assert value == 'grass'

    def test_evaluate_sentence_no_poke(self):
        truth = PokeTruth()
        with pytest.raises(NoPokemonFound):
            truth.evaluate_sentence(
                'Grass type pokemon and has 55 attack')

    def test_evaluate_sentence_demo_version(self):
        truth = PokeTruth()
        with pytest.raises(DemoVersionException):
            truth.evaluate_sentence(
                'Bulbasaur is grass type pokemon and Comfey is electric type')
