import re

from truthmeas.customexception import DemoVersionException, NoPokemonFound
from truthmeas.pokemons import poke_list, args_set
from truthmeas.request import get


class PokeTruth:
    def __init__(self):
        self.sentence_type = []
        self.sentence = ""
        self.pokemon = ""
        self.argument = []
        self.value = []
        self.sentence_truth = []
        self.poke_counter = 0

    def evaluate_sentence(self, sentence):
        self.sentence = sentence
        sentence_list = re.split('; |, | and | also ', sentence)
        print(sentence_list)
        poke_set = set(poke_list)
        sent_iter = 0
        while sent_iter < len(sentence_list):
            self._evaluate_single_sentence(poke_set, sentence_list[sent_iter])
            if self.pokemon != "":
                pokemon_spec = get(pokemon=self.pokemon)
            else:
                raise NoPokemonFound
            self.sentence_truth.append(self._check_truth(pokemon_spec,
                                                         sent_iter))
            sent_iter += 1

    def _check_truth(self, pokemon_spec, iterp):
        arg = self.argument[iterp]
        if arg == 'evolve':
            arg = 'evolution'
        val = self.value[iterp]
        true_val = str(getattr(pokemon_spec, arg))
        if self.sentence_type[iterp]:
            var = true_val == val
        else:
            var = true_val != val
        if var:
            print(str(iterp + 1) + '. sentence is true')
            return True
        else:
            print(str(iterp + 1) + '. sentence is false. True value of ' +
                  arg + ' is ' + true_val)
            return False

    def _evaluate_single_sentence(self, poke_set, sentence):
        words = sentence.split()
        index = 0
        sen_flag = True
        for word in words:
            if word in args_set:
                self.argument.append(word)
                self.value.append(self._take_value(index, words))
            elif word in poke_set:
                self.pokemon = word
                self.poke_counter += 1
            elif word == 'not':
                sen_flag = False
                self.sentence_type.append(False)
            index += 1
        if self.poke_counter > 1:
            raise DemoVersionException('Demo version of PokeTruth'
                                       ' allows to evaluate sentence '
                                       'with only one Pokemon')
        if (sen_flag):
            self.sentence_type.append(True)

    def _take_value(self, index, words):
        list_lenght = len(words)
        try:
            if index + 1 == list_lenght or words[list_lenght - 1] == 'pokemon':
                return words[index - 1]
            else:
                return words[index + 2]
        except IndexError:
            print('Out of array, something went wrong.'
                  ' Try to assemble sentence once again.')
