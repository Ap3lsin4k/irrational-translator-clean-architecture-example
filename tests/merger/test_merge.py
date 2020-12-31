import pytest
from gateway.replace_service import Replacer
from model.gateway.merger_repository import MergerRepository
from model.gateway.merger_repository import merge_two_words
from model.interactor import UserStory

from tests.dummies.file_reader import Dummy
from tests.dummies.presenter_dummies import PresenterDummy


@pytest.fixture
def m() -> MergerRepository():
    return MergerRepository()

@pytest.fixture
def uc() -> UserStory:
    return UserStory(PresenterDummy, Dummy(), Replacer())


def test_merge_words(m):
    first = "Кiт"
    second = "Десь"
    res = merge_two_words(first, second)
    difference = {'Д', 'е', 'с', 'ь', 'К', 'i', 'т'}.symmetric_difference(res)
    assert difference == set()
    assert len(difference) == 0


def test_merge_two_lower_case_words(m):
    first = "кiт"
    second = "десь"
    res = merge_two_words(first, second)
    difference = {'к', 'i', 'т', 'д', 'е', 'с', 'ь'}.symmetric_difference(res)
    assert difference == set()
    assert len(difference) == 0


def test_merge_two_lists_when_one_is_empty(m):
    sentence = ["Максим"]
    second = [""]
    assert len(m.merge_two_lists_of_words(sentence, second)[0]) == 6
    first = []
    second = ["іди", "їсти"]
    a, b = m.merge_two_lists_of_words(first, second)
    assert len(a) == 3
    assert len(b) == 4


def test_merge_two_lists_when_sizes_are_3_and_4(m):
    a, b, c, d = m.merge_two_lists_of_words(["Але", "ж", "ти", "нажилася"], ["А", "я", "пішла"])
    assert len(a) == 3 + 1 - 1
    assert len(b) == 1 + 1
    assert len(c) == 2 + 5
    assert len(d) == 8 + 0 - 1


def test_merge_two_lists_of_words_with_different_len(m):
    vector_of_words = m.merge_two_lists_of_words(("ходи", "доню", "до", "мене", "щось", "маю", "казати"),
                                                 ("чує", "Марина", "кличе", "її", "мати"))
    assert vector_of_words[0] == {'х', 'о', 'д', 'и', 'ч', 'у', 'є'}
    assert vector_of_words[3] == {'м', 'е', 'н', 'ї'}
    assert vector_of_words[5] == {'м', 'а', 'ю'}


def test_return_empty_strings_when_input_is_invalid(m):
    res = m.merge_two_lists_of_words([], [])
    assert len(res) == 0
    assert not bool(res)


@pytest.mark.skip("TODO")
def test_merge_two_sentences_with_punctuation_long():
    #
    first_sentence = """Кiт скочив з печi пiд пiл, неначе  його  хто  потяг  дубцем,  а
пiвень засокотав, заляпав крилами й  заспiвав."""
    second_sentence = """  Десь  у  кутку  задзижчала
муха. Весела Марина сполохала сонну хату; все  живе  в  хатi  знов  ожило,
прокинулось, зашумiло, загомонiло."""
    result = []
    assert isinstance(result[0], set)
    pass


def test_merge_two_sentences_with_punctuation():
    first_sentence = """Весела Марина сполохала сонну хату; все  живе  в  хатi  знов  ожило,
прокинулось, зашумiло, загомонiло."""
    second_sentence = """  Десь  у  кутку  задзижчала
муха."""
    uc = UserStory(None, None, None)

    sentence = uc.merge_two_sentences(first_sentence, second_sentence)
    assert sentence[0] == {'Д', 'е', 'с', 'ь', 'В', 'е', 'с', 'л', 'а'}
    assert sentence[3] == set('соннузадзижчала')
    assert sentence[4] == {'х', 'а', 'т', 'у', 'м'}




@pytest.mark.skip("Should do unit test before testing integration")
def test_merge_words_for_three_sentences_integration_test():
    me = MergerRepository
    text = """небi. Як,  заворушились  на
улицях люди; бiжать на базар мiщанки з  кошиками,  по  мостовiй  деркотять
звощики. Пiд шинком лежить, нiчого не чує Марина."""




# !?...




# def test_extend_with_new_words(use_cases):
#    with pytest.raises(KeyError):
#        use_cases.classify("добрий")