from src.entity_part_of_speech.presentation.ua_lang_presenter import UkrainianLanguagePresenter

from entity_part_of_speech.bookmark_entity import Bookmark
from entity_part_of_speech.language_interactor import UkrainianLanguageInteractor

ua_lang = UkrainianLanguageInteractor({
    'іменник': {
        'відміна': {
            'перша':
                ("дівчина", "ледащо", "сирота", "нероба", "розбишака", "бідолаха", "староста"),
            'друга':
                ("хлопець", "потяг", "життя", "почуття", "право", "місто", "місце", "прислів'я", "каменяр"),
            'третя':
                ("нехворощ", "любов", "мати"),
            'четверта':
                ("ягня",)
        }
    },
})
presenter = UkrainianLanguagePresenter()


class Controller:

    def execute(self):
        command = input("> ")
        if command == 'help' or command == '"help"' or command == 'help()':
            self.__print_manual()
        elif 'new' in command:
            self.extend_dictionary()
        elif 'edit' in command:
            self.edit_dictionary()
        else:
            self.__make_request(command)
        print()

    def __print_manual(self):
        print("Введіть слово, щоб подивитися характеристику.")
        print("При введені характеристики, програма виведе приклад слів.")
        print("Ключове слово \"new\" без лапок, щоб додати нові слова у словник.")
        print("Ключове слово \"edit\" без лапок, щоб відредагувати існуюче слово нові слова у словник.")

    def __make_request(self, word_might_be_typo):
        try:
            presenter.print_properties(ua_lang.classify(word_might_be_typo))
        except (KeyError, ValueError) as msg:
            presenter.error_messages.append(str(msg))
            try:
                presenter.print_words_as_examples(*ua_lang.get_examples(word_might_be_typo))
                presenter.error_messages.clear()
            except (KeyError, ValueError) as msg:
                if str(msg) not in presenter.error_messages:
                    presenter.error_messages.append(str(msg))
                presenter.print_error()
                presenter.print_suggestions_to_typo(ua_lang.construct_close_matches(word_might_be_typo))

    def extend_dictionary(self):
        part_of_speech = input('Введіть частину мови[прикметник]: ')
        category_name = input('Введіть за чим класифікувати слово[число]: ')
        property_name = input('Введіть до якої характеристики належить[множина]: ')

        print("Введіть слова розділені пробілом[зелена золотиста промениста неймовірна]")
        words = input(">>> ")

        print("Слова '{}' будуть додані до словника, частина мови — '{}', {} — {}."
              .format(words, part_of_speech, category_name, property_name))
        command = input("Підтвердити(так/ні): ")
        if command.lower() in ("так", "т", "y", "yes"):
            inp = {part_of_speech: {category_name: {property_name: tuple(words.split())}}}
            ua_lang.update(inp)
        else:
            print("Слово(а) не були додані до словника", words)

    def edit_dictionary(self):
        part_of_speech = input('Введіть частину мови[числівник]: ')
        category_name = input('Введіть за чим класифікувати слово[за значенням]: ')
        property_name = input('Введіть до якої характеристики належить[кількісний]: ')
        old_word = input("Введіть поточне слово[єдин]: ")
        new_word = input("Введіть нове слово[один]: ")
        print("Замінити слово '{}' на '{}'.".format(old_word, new_word))
        command = input("Підтвердити(так/ні): ")
        if command.lower() in ("так", "т", "y", "yes"):
            bm = Bookmark(part_of_speech, category_name, property_name)
            ua_lang.modify(bm, old_word, new_word)
        else:
            print("Скасовано")


