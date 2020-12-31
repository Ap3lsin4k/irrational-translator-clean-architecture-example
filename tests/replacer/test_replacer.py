import pytest
from gateway.replace_service import Replacer
from src import UserStory


def test_replace_small_letters():
    rl = Replacer()
    assert rl._replace_vowel_with_random_consonant_and_vice_versa('г') in "аеєиіїоуюя"
    assert rl._replace_vowel_with_random_consonant_and_vice_versa('а') in "бвгґджзйклмнпрстфхцчшщ"
    assert rl._replace_vowel_with_random_consonant_and_vice_versa('т') in "аеєиіїоуюя"


def test_upper_case_letters():
    rl = Replacer()
    assert rl._replace_vowel_with_random_consonant_and_vice_versa('Ю') in 'БВГҐДЖЗЙКЛМНПРСТФХЦЧШЩ'
    assert rl._replace_vowel_with_random_consonant_and_vice_versa('П') in 'АЕЄИІЇОУЮЯ'


def test_english_letters_as_ukrainian():
    rl = Replacer()
    assert rl._replace_vowel_with_random_consonant_and_vice_versa('i') in 'бвгґджзйклмнпрстфхцчшщ'


def test_ignore_sign():
    rl = Replacer()
    assert rl._replace_vowel_with_random_consonant_and_vice_versa('ь') == 'ь'
    assert rl._replace_vowel_with_random_consonant_and_vice_versa('Ь') == 'Ь'
    assert rl._replace_vowel_with_random_consonant_and_vice_versa('.') == '.'


def test_replace_each_letter_in_text():
    rl = Replacer()
    res = rl.replace_vowels_with_consonant("дит")
    assert res[0] in "аеєиіїоуюя"
