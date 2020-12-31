import pickle

from src.model.gateway.cucumber import Cucumber
from src.other.kyiv_dictionary_entity import KyivDictionary


class UserStory:
    def __init__(self, presenter, text_reader, replacer, merger):
        self.presenter = presenter
        self.text_reader = text_reader
        self.replacer = replacer
        self.merger_service = merger
        self.cucumber = Cucumber(KyivDictionary())


    def modify_sentences_in_text(self):
        try:
            text = self.text_reader.read()
        except FileNotFoundError as e:
            self.presenter.present_error(e)
        else:
            self.presenter.present(self.merger_service.merged_sentences)

    def execute_replacer(self):
        try:
            text = self.text_reader.read()
        except FileNotFoundError as e:
            self.presenter.present_error(e)
        else:
            self.replacer.replace_vowels_with_consonants(text)

    def make_directories(self):
        if self.text_reader.made_working_directory("C:/lab7/"):
            print("Info: 'lab7/' folder was created in C:/")

        if self.text_reader.made_working_directory("C:/lab7/Fedorko"):
            print("Info: 'Fedorko/' folder was created in C:/lab7/")
            print("Please put '23.txt' file inside 'C:/lab7/Fedorko")

        if self.text_reader.made_working_directory("C:/lab5/"):
            print("Info: 'lab5/' folder was created in C:/")

        if self.text_reader.made_working_directory("C:/lab6/"):
            print("Info: 'lab6/' folder was created in C:/")

    def execute_lab5_kyiv_dictionary(self):
        self.cucumber.save_kyiv_dictionary("E:/lab5/initial.kd")

        self.cucumber.load_kyiv_dictionary_from_default_path(r"E:/lab5/initial.kd")

        self.cucumber.extend_kyiv_dictionary({'л': {'lackey ': ['menial', 'retainer', 'servant', 'slavey', 'steward', 'dependable', 'reliable', 'responsible']}})

        self.cucumber.save_kyiv_dictionary("E:/lab5/updated dictionary.kd")

    def execute_lab6_parts_of_speech_in_ukrainian_language(self):
        pass
