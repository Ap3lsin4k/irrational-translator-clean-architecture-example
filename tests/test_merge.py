import pytest
from model.gateway.merger_repository import MergerRepository
from model.gateway.merger_repository import merge_two_words
from model.interactor import UserStory


@pytest.fixture
def m() -> MergerRepository(UserStory):
    return MergerRepository(UserStory)



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
    uc = UserStory()

    sentence = uc.merge_two_sentences(first_sentence, second_sentence)
    assert sentence[0] == {'Д', 'е', 'с', 'ь', 'В', 'е', 'с', 'л', 'а'}
    assert sentence[3] == set('соннузадзижчала')
    assert sentence[4] == {'х', 'а', 'т', 'у', 'м'}


def test_merge_words_for_three_sentences_unit_test(m):
    m.pair_and_merge_sentences(['г ', ' очей', 'коло сочi з '])
    assert m.merged_sentences[0][0] == set('очейг')
    assert m.merged_sentences[1] == [set("коло"), set("сочi"), {"з"}]


def test_pair_and_merge_three_trivial_sentences(m):
    m.pair_and_merge_sentences(['а', 'б', 'в'])
    assert m.merged_sentences[0][0] == {'а', 'б'}
    assert m.merged_sentences[1][0] == {'в'}
    assert len(m.merged_sentences) == 2


def test_merge_three_one_sentence_with_itself(m):
    m.pair_and_merge_sentences(('вда',))

    assert m.merged_sentences[0][0] == {'в','д','а'}
    assert len(m.merged_sentences) == 1


def test_pair_and_merge_text_that_becomes_empty(m):
    m.pair_and_merge_sentences(("",))
    assert m.merged_sentences[0] == []
    assert len(m.merged_sentences) == 1


def test_pair_and_merge_non_existing_text(m):
    m.pair_and_merge_sentences(tuple())
    assert not m.merged_sentences
    assert len(m.merged_sentences) == 0


def test_merge_two_sentences(m):
    m.pair_and_merge_sentences(('завсь на лиця', 'уз о ла'))
    assert m.merged_sentences[0][0] == {'з','а','в','с','ь','у'}
    assert m.merged_sentences[0][1] == {'н','а','о'}
    assert m.merged_sentences[0][2] == {'л','и','ц','я','л','а'}
    assert len(m.merged_sentences) == 1
    assert len(m.merged_sentences[0]) == 3


def test_merge_four_clean_sentences(m):
    m.pair_and_merge_sentences(('завсь на лиця', 'уз о ла',
                                'ах  май  жа  го  в  чер', 'Лих ск не маю'))
    assert m.merged_sentences[0][0] == {'з','а','в','с','ь','у'}
    assert m.merged_sentences[0][1] == {'н','а','о'}
    assert m.merged_sentences[0][2] == {'л','и','ц','я','л','а'}
    assert m.merged_sentences[1][0] == {'а','х','Л','и','х'}
    assert m.merged_sentences[1][1] == {'м',"а","й", "с", "к"}
    assert m.merged_sentences[1][3] == set('гомаю')
    assert m.merged_sentences[1][4] == {"в"}
    assert m.merged_sentences[1][5] == {"ч","е","р"}


def test_merge_five_clean_sentences(m):
    m.pair_and_merge_sentences(("в сй гдi", "Тебе ж люди оь",
                                "Як схо", "Я не боюсь лго  пру",
                                "каже Ма"))
    assert m.merged_sentences[0][0] == {'Т','е','б','е','в'}
    assert m.merged_sentences[0][1] == {'с', 'й', 'ж'}
    assert len(m.merged_sentences[0]) == 4
    assert len(m.merged_sentences[1]) == 5
    assert m.merged_sentences[2][0] == set("каже")
    assert m.merged_sentences[2][1] == {'М', 'а'}
    assert len(m.merged_sentences[2]) == 2
    assert len(m.merged_sentences) == 3


def test_must_clean_state_when_merging_for_the_second_time(m):
    m.pair_and_merge_sentences(('юб','ґс',
                                'і','в',    'і'))
    assert len(m.merged_sentences) == 3
    assert len(m.merged_sentences[0]) == 1
    assert (m.merged_sentences[0][0]) == {'ю','б', 'ґ', 'с'}

    m.pair_and_merge_sentences(('а', 'б'))

    assert len(m.merged_sentences) == 1

@pytest.mark.skip("")
def test_merge_seven_clean_sentences_and_then_merge_two():
  #  m.pair_and_merge_sentences('бо','л',
   #                             '','в',    'а','ф')
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


@pytest.mark.skip("TODO in presenter")
def test_merge_two_sentences_and_return_strings():
    pass

# def test_extend_with_new_words(use_cases):
#    with pytest.raises(KeyError):
#        use_cases.classify("добрий")

# TODO don't keep the punctuation
