import pytest
from model.interactor import UserStory


@pytest.fixture
def uc() -> UserStory():
    return UserStory()


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
