import random


class Replacer(object):
    def __init__(self):
        self.vowels = set('аеєиіїоуюяiceoa')
        self.vowels_upper_case = set('АЕЄИІЇОУЮЯICEOA')
        self.consonants = set('бвгґджзйклмнпрстфхцчшщ')
        self.consonants_upper_case = set('БВГҐДЖЗЙКЛМНПРСТФХЦЧШЩ')

    def _replace_vowel_with_random_consonant_and_vice_versa(self, letter):
        if letter.isupper():
            if letter in self.vowels_upper_case:
                return random.choice('БВГҐДЖЗЙКЛМНПРСТФХЦЧШЩ')
            elif letter in self.consonants_upper_case:
                return random.choice('АЕЄИІЇОУЮЯ')
        else:
            if letter in self.vowels:
                return random.choice('бвгґджзйклмнпрстфхцчшщ')
            elif letter in self.consonants:
                return random.choice("аеєиіїоуюя")
        return letter

    def replace_vowels_with_consonants(self, text):
        new_text = []
        for letter in text:
            new_text.append(self._replace_vowel_with_random_consonant_and_vice_versa(letter))

        return "".join(new_text)
