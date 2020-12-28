import pytest
from gateway.merger_repository import MergerRepository

from tests.fixtures.big_data_examples import whole_raw_text


@pytest.fixture
def r() -> MergerRepository():
    return MergerRepository()


def test_read(r):
    res = r.read_file_from_default_pathname()
    assert len(res) == len(whole_raw_text)


def test_merge_words(r):
    first = "Кiт"
    second = "Десь"
    res = r.merge_two_words(first, second)
    difference = {'Д', 'е', 'с', 'ь', 'К', 'i', 'т'}.symmetric_difference(res)
    assert difference == set()
    assert len(difference) == 0


def test_merge_two_lower_case_words(r):
    first = "кiт"
    second = "десь"
    res = r.merge_two_words(first, second)
    difference = {'к', 'i', 'т', 'д', 'е', 'с', 'ь'}.symmetric_difference(res)
    assert difference == set()
    assert len(difference) == 0


def test_merge_two_lists_when_one_is_empty(r):
    sentence = ["Максим"]
    second = [""]
    assert len(r.merge_two_lists_of_words(sentence, second)[0]) == 6
    first = []
    second = ["іди", "їсти"]
    a, b = r.merge_two_lists_of_words(first, second)
    assert len(a) == 3
    assert len(b) == 4


def test_merge_two_lists_when_sizes_are_3_and_4(r):
    a, b, c, d = r.merge_two_lists_of_words(["Але", "ж", "ти", "нажилася"], ["А", "я", "пішла"])
    assert len(a) == 3 + 1 - 1
    assert len(b) == 1 + 1
    assert len(c) == 2 + 5
    assert len(d) == 8 + 0 - 1


def test_merge_two_lists_of_words_with_different_len(r):
    vector_of_words = r.merge_two_lists_of_words(("ходи", "доню", "до", "мене", "щось", "маю", "казати"),
                                                 ("чує", "Марина", "кличе", "її", "мати"))
    assert vector_of_words[0] == {'х', 'о', 'д', 'и', 'ч', 'у', 'є'}
    assert vector_of_words[3] == {'м', 'е', 'н', 'ї'}
    assert vector_of_words[5] == {'м', 'а', 'ю'}


def test_return_empty_strings_when_input_is_invalid(r):
    res = r.merge_two_lists_of_words([], [])
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


def test_split_to_words(r):
    sentence_with_punctuation = """Весела Марина сполохала сонну хату; все  живе  в  хатi  знов  ожило,
    прокинулось, зашумiло, загомонiло."""
    result = r.split_to_words(sentence_with_punctuation)
    assert result[0] == 'Весела'
    assert result[1] == 'Марина'
    assert result[4] == 'хату'
    assert result[5] == 'все'
    assert result[10] == 'ожило'
    assert result[11] == 'прокинулось'
    assert result[12] == 'зашумiло'
    assert result[13] == 'загомонiло'
    assert len(result) == 14


def test_merge_two_sentences_with_punctuation(r):
    first_sentence = """Весела Марина сполохала сонну хату; все  живе  в  хатi  знов  ожило,
прокинулось, зашумiло, загомонiло."""
    second_sentence = """  Десь  у  кутку  задзижчала
муха."""
    sentence = r.merge_two_sentences(first_sentence, second_sentence)
    assert sentence[0] == {'Д', 'е', 'с', 'ь', 'В', 'е', 'с', 'л', 'а'}
    assert sentence[3] == set('соннузадзижчала')
    assert sentence[4] == {'х', 'а', 'т', 'у', 'м'}


def test_merge_two_sentences_with_quote_punctuation_marks(r):
    first = """Перехрестились й прочитали за
покiй душi "Отченаш" навiть вороги Марининi."""
    second = """"Не втекла, - кажуть, -  таки
од свого лиха, i не загуляла, й не заспiвала, й не затанцювала його навiть
в Києвi"."""
    sentence = r.merge_two_sentences(first, second)
    assert sentence[0] == {'П', 'е', 'р', 'е', 'х', 'р', 'е', 'с', 'т', 'и', 'л', 'и', 'с', 'ь', 'Н'}
    assert sentence[1] == set("йвтекла")
    assert sentence[2] == set("прочиталкажуь")
    assert sentence[3] == set("затаки")
    assert sentence[-1] == {'К','и','є','в','i'}
    assert sentence[19] == {'К','и','є','в','i'}
    assert len(sentence) == 20


def test_merge_text_with_two_sentences_remove_punctuation(r):
    text = """Iван Нечуй-Левицький. Двi московки


V _"""
    re = MergerRepository()

    words = re.merge_pairs_of_sentences_in_text(text)
    assert words[0] == {'I','в','а','н', 'Д','в','i'}
    assert words[1] == {'Н','е','ч','у','й', 'м','о','с','к','о','в','к','и','Л','е','в','и','ц','ь','к','й'}
    with pytest.raises(IndexError):
        assert words[2] is None
    assert len(words) == 2
#    assert len(words) == 3
    #assert words[1] == {'I', 'в', 'а', 'н', 'Д', 'в', 'i'}


@pytest.mark.skip("TODO")
def test_split_text_to_pairs_of_sentences():
    pass


@pytest.mark.skip("TODO")
def test_newline():
    pass


@pytest.mark.skip("TODO")
def test_capital_character():
    pass


@pytest.mark.skip("TODO")
def test_make_pairs_of_sentences_with_question_mark_and_exclemation_mark_or_three_dots():
    pass


# !?...
@pytest.mark.skip("TODO")
def test_filter_out_dash_underscore_comma_semicolon():
    pass


@pytest.mark.skip("TODO in presenter")
def test_merge_two_sentences_and_return_strings():
    pass

# def test_extend_with_new_words(use_cases):
#    with pytest.raises(KeyError):
#        use_cases.classify("добрий")

# TODO ask whether I need to lower all the other letters,
# TODO should I keep punctuation
