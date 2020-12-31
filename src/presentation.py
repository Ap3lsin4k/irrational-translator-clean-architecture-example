import builtins


class Presenter:
    def __init__(self, view):
        self.view = view

    def present(self, response_model):
        for sentence in response_model:
            self.present_sentence(sentence)

    def present_sentence(self, sentence):
        presentable = list(map(self.__container_to_str, sentence))
        presentable[0] = presentable[0].capitalize()
        self.view.print(*presentable, '\n')

    @staticmethod
    def __container_to_str(each_character_as_array_element):
        return "".join(each_character_as_array_element)

    def present_error(self, printable):
        builtins.print(printable)