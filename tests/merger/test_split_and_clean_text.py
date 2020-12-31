import pytest
from model.gateway.clean_and_split_text_repository import CleanAndSplitTextRepository


@pytest.fixture
def cleaner() -> CleanAndSplitTextRepository():
    return CleanAndSplitTextRepository()


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


@pytest.mark.skip("TODO")
def test_filter_out_dash_underscore_comma_semicolon():
    pass


def test_split_three_sentences():
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
