from src import Replacer


class ReplacerDummy(Replacer):
    def replace_vowels_with_consonants(self, kwargs):
        return None

    def _replace_vowel_with_random_consonant_and_vice_versa(self, **kwargs): pass