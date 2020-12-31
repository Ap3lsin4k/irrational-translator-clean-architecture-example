import pytest

from presentation import Presenter


class ViewSpy:
    last_message = ""

    def print(self, *args, sep=' ', end='\n', file=None):
        if file is not None:
            raise NotImplementedError

        self.last_message = sep.join(map(str, args)) + end


def test_view():
    v = ViewSpy()
    v.print("nothing")
    assert v.last_message == "nothing\n"

    v.print("something")
    assert v.last_message == "something\n"

    v.print("John", "Smith")
    assert v.last_message == "John Smith\n"

    v.print("apples", 24, "grapes", "bananas", sep=',')
    assert v.last_message == "apples,24,grapes,bananas\n"

    v.print("Automated testing is fun", end='!!!')
    assert v.last_message == "Automated testing is fun!!!"

    v.print("Maybe, you don't need a new line", end='')
    assert v.last_message == "Maybe, you don't need a new line"


def test_present_sentence():
    view = ViewSpy()
    p = Presenter(view)
    p.present_sentence(({'ь', 'е', 'с', 'Д', 'В', 'л', 'а'}, {'М', 'у', 'и', 'р', 'а', 'н'},
                        {'п', 'х', 'к', 'у', 'т', 'о', 'л', 'а', 'с'},
                        {'и', 'д', 'н', 'ч', 'у', 'з', 'ж', 'о', 'л', 'а', 'с'}, {'х', 'у', 'т', 'а', 'м'},
                        {'в', 'е', 'с'}, {'в', 'е', 'и', 'ж'}, {'в'}, {'х', 'т', 'i', 'а'}, {'в', 'о', 'з', 'н'},
                        {'и', 'л', 'ж', 'о'}, {'п', 'ь', 'и', 'р', 'н', 'к', 'у', 'о', 'л', 'с'},
                        {'ш', 'i', 'у', 'з', 'о', 'л', 'а', 'м'}, {'i', 'г', 'н', 'з', 'о', 'л', 'а', 'м'}))

    printed_words = view.last_message.split()
    first_word = view.last_message.split()[0]
    assert len(printed_words) == 14

    assert len(first_word) == 7
    for letter in first_word:
        assert letter.lower() in {'ь', 'е', 'с', 'д', 'в', 'л', 'а'}

    assert view.last_message[-1] == '\n'
    assert view.last_message[13] != ' '
    assert view.last_message[14] == ' '
    assert view.last_message[15] != ' '

    third_word = printed_words[2]
    assert len(third_word) == 9
    for letter in third_word:
        assert letter in {'п', 'х', 'к', 'у', 'т', 'о', 'л', 'а', 'с'}


def test_capitalize():
    view = ViewSpy()
    p = Presenter(view)
    p.present_sentence(({'ь'}, {'а', 'н'},
                        {'п', 'х'}))
    assert view.last_message[0] == 'Ь'
    assert view.last_message[-1] == '\n'

def test_capitilize_and_newline():
    pass

@pytest.mark.skip("TODO")
def test_capital_character():
    pass
@pytest.mark.skip("TODO in presenter")
def test_merge_two_sentences_and_return_strings():
    pass

@pytest.mark.skip("TODO in presenter")
def test_error_printing_if_file_was_not_found_or_directory_was_not_created():
    pass

@pytest.mark.skip("Test newline is only one")
def test_nothing():
    pass