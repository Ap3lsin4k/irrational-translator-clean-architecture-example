import builtins
import pytest


class ViewSpy:
    last_message = ""

    def print(self, *args, sep=' ', end='\n', file=None):
        if file is not None:
            raise NotImplementedError

        self.last_message = sep.join(map(str, args)) + end


class Presenter:
    def __init__(self, view):
        self.view = view

    def present_sentence(self, response_model):
        self.view.print(*map(self.__container_to_str, response_model))

    @staticmethod
    def __container_to_str(each_character_as_array_element):
        return "".join(each_character_as_array_element)

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
        assert letter in {'ь', 'е', 'с', 'Д', 'В', 'л', 'а'}

    assert view.last_message[-1] == '\n'
    assert view.last_message[13] != ' '
    assert view.last_message[14] == ' '
    assert view.last_message[15] != ' '

    third_word = printed_words[2]
    assert len(third_word) == 9
    for letter in third_word:
        assert letter in {'п', 'х', 'к', 'у', 'т', 'о', 'л', 'а', 'с'}


# TODO use file writer to save messages into the file in presenter
