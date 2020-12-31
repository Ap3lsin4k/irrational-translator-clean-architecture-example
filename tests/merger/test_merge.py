import pytest
from model.gateway.merger import MergerService
from model.gateway.merger import merge_two_words


@pytest.fixture
def merger() -> MergerService():
    return MergerService()



def test_merge_words(merger):
    first = "Кiт"
    second = "Десь"
    res = merge_two_words(first, second)
    difference = {'Д', 'е', 'с', 'ь', 'К', 'i', 'т'}.symmetric_difference(res)
    assert difference == set()
    assert len(difference) == 0


def test_merge_two_lower_case_words(merger):
    first = "кiт"
    second = "десь"
    res = merge_two_words(first, second)
    difference = {'к', 'i', 'т', 'д', 'е', 'с', 'ь'}.symmetric_difference(res)
    assert difference == set()
    assert len(difference) == 0


def test_merge_two_lists_when_one_is_empty(merger):
    sentence = ["Максим"]
    second = [""]
    assert len(merger.merge_two_lists_of_words(sentence, second)[0]) == 6
    first = []
    second = ["іди", "їсти"]
    a, b = merger.merge_two_lists_of_words(first, second)
    assert len(a) == 3
    assert len(b) == 4


def test_merge_two_lists_when_sizes_are_3_and_4(merger):
    a, b, c, d = merger.merge_two_lists_of_words(["Але", "ж", "ти", "нажилася"], ["А", "я", "пішла"])
    assert len(a) == 3 + 1 - 1
    assert len(b) == 1 + 1
    assert len(c) == 2 + 5
    assert len(d) == 8 + 0 - 1


def test_merge_two_lists_of_words_with_different_len(merger):
    vector_of_words = merger.merge_two_lists_of_words(("ходи", "доню", "до", "мене", "щось", "маю", "казати"),
                                                 ("чує", "Марина", "кличе", "її", "мати"))
    assert vector_of_words[0] == {'х', 'о', 'д', 'и', 'ч', 'у', 'є'}
    assert vector_of_words[3] == {'м', 'е', 'н', 'ї'}
    assert vector_of_words[5] == {'м', 'а', 'ю'}


def test_return_empty_strings_when_input_is_invalid(merger):
    res = merger.merge_two_lists_of_words([], [])
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
    uc = MergerService()

    sentence = uc.merge_two_sentences(first_sentence, second_sentence)
    assert sentence[0] == {'Д', 'е', 'с', 'ь', 'В', 'е', 'с', 'л', 'а'}
    assert sentence[3] == set('соннузадзижчала')
    assert sentence[4] == {'х', 'а', 'т', 'у', 'м'}




@pytest.mark.skip("Should do unit test before testing integration")
def test_merge_words_for_three_sentences_integration_test():
    me = MergerService
    text = """небi. Як,  заворушились  на
улицях люди; бiжать на базар мiщанки з  кошиками,  по  мостовiй  деркотять
звощики. Пiд шинком лежить, нiчого не чує Марина."""





def test_merge_two_sentences_with_quote_punctuation_marks(merger):
    first = """Перехрестились й прочитали за
покiй душi "Отченаш" навiть вороги Марининi."""
    second = """"Не втекла, - кажуть, -  таки
од свого лиха, i не загуляла, й не заспiвала, й не затанцювала його навiть
в Києвi"."""
    sentence = merger.merge_two_sentences(first, second)
    assert sentence[0] == {'П', 'е', 'р', 'е', 'х', 'р', 'е', 'с', 'т', 'и', 'л', 'и', 'с', 'ь', 'Н'}
    assert sentence[1] == set("йвтекла")
    assert sentence[2] == set("прочиталкажуь")
    assert sentence[3] == set("затаки")
    assert sentence[-1] == {'К', 'и', 'є', 'в', 'i'}
    assert sentence[19] == {'К', 'и', 'є', 'в', 'i'}
    assert len(sentence) == 20


def test_merge_text_with_two_sentences_remove_punctuation(merger):
    text = """Iван Нечуй-Левицький. Двi московки


V _"""

    words = merger.split_text_to_sentences_and_merge_them(text)[0]
    assert words[0] == {'I', 'в', 'а', 'н', 'Д', 'в', 'i'}
    assert words[1] == {'Н', 'е', 'ч', 'у', 'й', 'м', 'о', 'с', 'к', 'о', 'в', 'к', 'и'}
    assert words[2] == {'Л', 'е', 'в', 'и', 'ц', 'ь', 'к', 'й'}
    with pytest.raises(IndexError):
        assert words[3] is None


def test_split_text_and_merge_sentences(merger):
    text = """В у та дзвiн. Гуляє 
по ,  .  Нiквi.Одна  Га
а з ,   , i  попiд .
   "Аде ж мене  до себе , - за Га. - З на чк,
пожу,.      ",  -      i
 до  . у  в   полум'я,  
 i б'є, т i  
та ."""
    presenter_spy = merger.split_text_to_sentences_and_merge_them(text)
    assert presenter_spy[0][0] == set("ГуляєВ")
    assert presenter_spy[0][1] == set("упо")


def test_merge_five_clean_sentences(merger):
    merger.pair_sentences(("в сй гдi", "Тебе ж люди оь",
                           "Як схо", "Я не боюсь лго  пру",
                           "каже Ма"))
    assert merger.merged_sentences[0][0] == {'Т', 'е', 'б', 'е', 'в'}
    assert merger.merged_sentences[0][1] == {'с', 'й', 'ж'}
    assert len(merger.merged_sentences[0]) == 4
    assert len(merger.merged_sentences[1]) == 5
    assert merger.merged_sentences[2][0] == set("каже")
    assert merger.merged_sentences[2][1] == {'М', 'а'}
    assert len(merger.merged_sentences[2]) == 2
    assert len(merger.merged_sentences) == 3


def test_must_clean_state_when_merging_for_the_second_time(merger):
    merger.pair_sentences(('юб', 'ґс',
                           'і', 'в', 'і'))
    assert len(merger.merged_sentences) == 3
    assert len(merger.merged_sentences[0]) == 1
    assert (merger.merged_sentences[0][0]) == {'ю', 'б', 'ґ', 'с'}

    merger.pair_sentences(('а', 'б'))

    assert len(merger.merged_sentences) == 1


def test_merge_words_for_three_sentences_unit_test(merger):
    merger.pair_sentences(['г ', ' очей', 'коло сочi з '])
    assert merger.merged_sentences[0][0] == set('очейг')
    assert merger.merged_sentences[1] == [set("коло"), set("сочi"), {"з"}]


def test_pair_and_merge_three_trivial_sentences(merger):
    merger.pair_sentences(['а', 'б', 'в'])
    assert merger.merged_sentences[0][0] == {'а', 'б'}
    assert merger.merged_sentences[1][0] == {'в'}
    assert len(merger.merged_sentences) == 2


def test_merge_three_one_sentence_with_itself(merger):
    merger.pair_sentences(('вда',))

    assert merger.merged_sentences[0][0] == {'в', 'д', 'а'}
    assert len(merger.merged_sentences) == 1


def test_pair_and_merge_text_that_becomes_empty(merger):
    merger.pair_sentences(("",))
    assert merger.merged_sentences[0] == []
    assert len(merger.merged_sentences) == 1


def test_pair_and_merge_non_existing_text(merger):
    merger.pair_sentences(tuple())
    assert not merger.merged_sentences
    assert len(merger.merged_sentences) == 0


def test_merge_two_sentences(merger):
    merger.pair_sentences(('завсь на лиця', 'уз о ла'))
    assert merger.merged_sentences[0][0] == {'з', 'а', 'в', 'с', 'ь', 'у'}
    assert merger.merged_sentences[0][1] == {'н', 'а', 'о'}
    assert merger.merged_sentences[0][2] == {'л', 'и', 'ц', 'я', 'л', 'а'}
    assert len(merger.merged_sentences) == 1
    assert len(merger.merged_sentences[0]) == 3


def test_merge_four_clean_sentences(merger):
    merger.pair_sentences(('завсь на лиця', 'уз о ла',
                           'ах  май  жа  го  в  чер', 'Лих ск не маю'))
    assert merger.merged_sentences[0][0] == {'з', 'а', 'в', 'с', 'ь', 'у'}
    assert merger.merged_sentences[0][1] == {'н', 'а', 'о'}
    assert merger.merged_sentences[0][2] == {'л', 'и', 'ц', 'я', 'л', 'а'}
    assert merger.merged_sentences[1][0] == {'а', 'х', 'Л', 'и', 'х'}
    assert merger.merged_sentences[1][1] == {'м', "а", "й", "с", "к"}
    assert merger.merged_sentences[1][3] == set('гомаю')
    assert merger.merged_sentences[1][4] == {"в"}
    assert merger.merged_sentences[1][5] == {"ч", "е", "р"}


# !?...




# def test_extend_with_new_words(use_cases):
#    with pytest.raises(KeyError):
#        use_cases.classify("добрий")