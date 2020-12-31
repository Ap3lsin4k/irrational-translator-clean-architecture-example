import pytest
from model.interactor import UserStory

from tests.dummies.presenter_dummies import PresenterDummy


@pytest.fixture
def uc() -> UserStory:
    return UserStory(PresenterDummy(), None, None)


def test_merge_two_sentences_with_quote_punctuation_marks(uc):
    first = """Перехрестились й прочитали за
покiй душi "Отченаш" навiть вороги Марининi."""
    second = """"Не втекла, - кажуть, -  таки
од свого лиха, i не загуляла, й не заспiвала, й не затанцювала його навiть
в Києвi"."""
    sentence = uc.merge_two_sentences(first, second)
    assert sentence[0] == {'П', 'е', 'р', 'е', 'х', 'р', 'е', 'с', 'т', 'и', 'л', 'и', 'с', 'ь', 'Н'}
    assert sentence[1] == set("йвтекла")
    assert sentence[2] == set("прочиталкажуь")
    assert sentence[3] == set("затаки")
    assert sentence[-1] == {'К', 'и', 'є', 'в', 'i'}
    assert sentence[19] == {'К', 'и', 'є', 'в', 'i'}
    assert len(sentence) == 20


def test_merge_text_with_two_sentences_remove_punctuation(uc):
    text = """Iван Нечуй-Левицький. Двi московки


V _"""

    words = uc.split_text_to_sentences_and_merge_them(text)[0]
    assert words[0] == {'I', 'в', 'а', 'н', 'Д', 'в', 'i'}
    assert words[1] == {'Н', 'е', 'ч', 'у', 'й', 'м', 'о', 'с', 'к', 'о', 'в', 'к', 'и'}
    assert words[2] == {'Л', 'е', 'в', 'и', 'ц', 'ь', 'к', 'й'}
    with pytest.raises(IndexError):
        assert words[3] is None


def test_split_text_and_merge_sentences(uc):
    text = """В у та дзвiн. Гуляє 
по ,  .  Нiквi.Одна  Га
а з ,   , i  попiд .
   "Аде ж мене  до себе , - за Га. - З на чк,
пожу,.      ",  -      i
 до  . у  в   полум'я,  
 i б'є, т i  
та ."""
    presenter_spy = uc.split_text_to_sentences_and_merge_them(text)
    assert presenter_spy[0][0] == set("ГуляєВ")
    assert presenter_spy[0][1] == set("упо")


def test_merge_five_clean_sentences(uc):
    uc.pair_and_merge_sentences(("в сй гдi", "Тебе ж люди оь",
                                "Як схо", "Я не боюсь лго  пру",
                                "каже Ма"))
    assert uc.merged_sentences[0][0] == {'Т','е','б','е','в'}
    assert uc.merged_sentences[0][1] == {'с', 'й', 'ж'}
    assert len(uc.merged_sentences[0]) == 4
    assert len(uc.merged_sentences[1]) == 5
    assert uc.merged_sentences[2][0] == set("каже")
    assert uc.merged_sentences[2][1] == {'М', 'а'}
    assert len(uc.merged_sentences[2]) == 2
    assert len(uc.merged_sentences) == 3


def test_must_clean_state_when_merging_for_the_second_time(uc):
    uc.pair_and_merge_sentences(('юб','ґс',
                                'і','в',    'і'))
    assert len(uc.merged_sentences) == 3
    assert len(uc.merged_sentences[0]) == 1
    assert (uc.merged_sentences[0][0]) == {'ю','б', 'ґ', 'с'}

    uc.pair_and_merge_sentences(('а', 'б'))

    assert len(uc.merged_sentences) == 1


def test_merge_words_for_three_sentences_unit_test(uc):
    uc.pair_and_merge_sentences(['г ', ' очей', 'коло сочi з '])
    assert uc.merged_sentences[0][0] == set('очейг')
    assert uc.merged_sentences[1] == [set("коло"), set("сочi"), {"з"}]


def test_pair_and_merge_three_trivial_sentences(uc):
    uc.pair_and_merge_sentences(['а', 'б', 'в'])
    assert uc.merged_sentences[0][0] == {'а', 'б'}
    assert uc.merged_sentences[1][0] == {'в'}
    assert len(uc.merged_sentences) == 2


def test_merge_three_one_sentence_with_itself(uc):
    uc.pair_and_merge_sentences(('вда',))

    assert uc.merged_sentences[0][0] == {'в','д','а'}
    assert len(uc.merged_sentences) == 1


def test_pair_and_merge_text_that_becomes_empty(uc):
    uc.pair_and_merge_sentences(("",))
    assert uc.merged_sentences[0] == []
    assert len(uc.merged_sentences) == 1


def test_pair_and_merge_non_existing_text(uc):
    uc.pair_and_merge_sentences(tuple())
    assert not uc.merged_sentences
    assert len(uc.merged_sentences) == 0


def test_merge_two_sentences(uc):
    uc.pair_and_merge_sentences(('завсь на лиця', 'уз о ла'))
    assert uc.merged_sentences[0][0] == {'з','а','в','с','ь','у'}
    assert uc.merged_sentences[0][1] == {'н','а','о'}
    assert uc.merged_sentences[0][2] == {'л','и','ц','я','л','а'}
    assert len(uc.merged_sentences) == 1
    assert len(uc.merged_sentences[0]) == 3


def test_merge_four_clean_sentences(uc):
    uc.pair_and_merge_sentences(('завсь на лиця', 'уз о ла',
                                'ах  май  жа  го  в  чер', 'Лих ск не маю'))
    assert uc.merged_sentences[0][0] == {'з','а','в','с','ь','у'}
    assert uc.merged_sentences[0][1] == {'н','а','о'}
    assert uc.merged_sentences[0][2] == {'л','и','ц','я','л','а'}
    assert uc.merged_sentences[1][0] == {'а','х','Л','и','х'}
    assert uc.merged_sentences[1][1] == {'м',"а","й", "с", "к"}
    assert uc.merged_sentences[1][3] == set('гомаю')
    assert uc.merged_sentences[1][4] == {"в"}
    assert uc.merged_sentences[1][5] == {"ч","е","р"}