import pytest
from gateway.merger_repository import *


@pytest.fixture
def r() -> MergerRepository():
    return MergerRepository()

@pytest.fixture
def cleaner() -> CleanAndSplitTextRepository():
    return CleanAndSplitTextRepository()


def test_merge_words(r):
    first = "Кiт"
    second = "Десь"
    res = merge_two_words(first, second)
    difference = {'Д', 'е', 'с', 'ь', 'К', 'i', 'т'}.symmetric_difference(res)
    assert difference == set()
    assert len(difference) == 0


def test_merge_two_lower_case_words(r):
    first = "кiт"
    second = "десь"
    res = merge_two_words(first, second)
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


def test_split_to_words(cleaner):
    sentence_with_punctuation = """Весела Марина сполохала сонну хату; все  живе  в  хатi  знов  ожило,
    прокинулось, зашумiло, загомонiло."""
    result = cleaner.split_to_words(sentence_with_punctuation)
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
    assert sentence[-1] == {'К', 'и', 'є', 'в', 'i'}
    assert sentence[19] == {'К', 'и', 'є', 'в', 'i'}
    assert len(sentence) == 20


def test_merge_text_with_two_sentences_remove_punctuation(r):
    text = """Iван Нечуй-Левицький. Двi московки


V _"""

    words = r.merge_pairs_of_sentences_in_text(text)
    assert words[0] == {'I', 'в', 'а', 'н', 'Д', 'в', 'i'}
    assert words[1] == {'Н', 'е', 'ч', 'у', 'й', 'м', 'о', 'с', 'к', 'о', 'в', 'к', 'и', 'Л', 'е', 'в', 'и', 'ц', 'ь',
                        'к', 'й'}
    with pytest.raises(IndexError):
        assert words[2] is None
    assert len(words) == 2


def test_split_three_sentences(r):
    text = """Не зрозумiю, сину, що ти говориш. Тобто ти паном будеш, чи що?
   - Так, так, матушко."""
    cl = CleanAndSplitTextRepository()
    cl.split_to_clean_sentences(text)
    res = cl.sentences_list
    assert res[0] == "Не зрозумiю  сину  що ти говориш"
    assert res[1] == " Тобто ти паном будеш  чи що"
    assert res[2] == "      Так  так  матушко"
    with pytest.raises(IndexError):
        assert res[3] is None


#  assert len(res) ==


def test_do_not_spoil_one_sentence_in_text(cleaner):
    text = "На"
    cleaner.split_to_clean_sentences(text)
    assert cleaner.sentences_list[0] == "На"
    assert len(cleaner.sentences_list) == 1


def test_make_pairs_of_sentences_with_exclemation_mark(cleaner):
    text = """На, на полу, на печi,як  хмара, та
хлопцi! Смiх, регiт, жарти та спiви"""
    cleaner.split_to_clean_sentences(text)
    two_sentences = cleaner.sentences_list
    assert two_sentences[0] == "На  на полу  на печi як  хмара  та хлопцi"
    assert two_sentences[1] == " Смiх  регiт  жарти та спiви"
    with pytest.raises(IndexError):
        print(two_sentences[3])


def test_halve_text_with_three_dots(cleaner):
    text = """Чи...сказала"""
    cleaner.split_to_clean_sentences(text)
    assert cleaner.sentences_list == ['Чи', 'сказала']


def test_replace_newline_with_whitespace(cleaner):
    text = """Одвернула вона й закрила своє лице.
   Пройшла,. за
пi. и
одi"."""
    assert cleaner.sentences_list == []
    cleaner.split_to_clean_sentences(text)
    assert cleaner.sentences_list[0] == 'Одвернула вона й закрила своє лице'
    assert cleaner.sentences_list[1] == '    Пройшла '
    assert cleaner.sentences_list[2] == ' за пi'
    assert cleaner.sentences_list[3] == ' и одi '


def test_merge_words_for_three_sentences_unit_test():
    me = MergerRepository()
    text = """небi. Як,  заворушились  на
    улицях люди; бiжать на базар мiщанки з  кошиками,  по  мостовiй  деркотять
    звощики. Пiд шинком лежить, нiчого не чує Марина."""
    me.pair_and_merge_sentences(['г ', ' очей', 'коло сочi з '])
    assert me.merged_sentences[0] == [set('очейг')]
    assert me.merged_sentences[1] == [set("коло"), set("сочi"), {"з"}]

@pytest.mark.skip("Don't go for the gold first")
def test_pair_and_merge_zero_sentences_or_one():
    pass


@pytest.mark.skip("Should do unit test before testing integration")
def test_merge_words_for_three_sentences_integration_test():
    me = MergerRepository
    text = """небi. Як,  заворушились  на
улицях люди; бiжать на базар мiщанки з  кошиками,  по  мостовiй  деркотять
звощики. Пiд шинком лежить, нiчого не чує Марина."""

@pytest.mark.skip("TODO")
def test_capital_character():
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
