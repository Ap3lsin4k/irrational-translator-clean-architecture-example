import pickle

from src.entity_part_of_speech.presentation.ua_lang_controller import ua_lang

from model.gateway.library import Library
from src.model.gateway.cucumber import Cucumber
from src.other.kyiv_dictionary_entity import KyivDictionary


class UserStory:
    def __init__(self, presenter, text_reader, replacer, merger):
        self.presenter = presenter
        self.text_reader = text_reader
        self.replacer = replacer
        self.merger_service = merger
        self.cucumber = Cucumber(KyivDictionary())
        self.library = Library(ua_lang)


    def modify_sentences_in_text(self):
        try:
            text = self.text_reader.read()
        except FileNotFoundError as e:
            self.presenter.present_error(e)
        else:
            self.merger_service.split_text_to_sentences_and_merge_them(text)
            self.presenter.present(self.merger_service.merged_sentences)

    def execute_replacer(self):
        try:
            text = self.text_reader.read()
        except FileNotFoundError as e:
            self.presenter.present_error(e)
        else:
            self.text_reader.write(self.replacer.replace_vowels_with_consonants(text), path='C:/lab7/Fedorko/232.txt')

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
        self.cucumber.save_kyiv_dictionary("C:/lab5/initial.kd")
        self.presenter.present_saving_dictionary("Kyiv Dictionary (lab 5)", "C:/lab5/initial.kd", self.cucumber.kyiv_dictionary)

        self.cucumber.load_kyiv_dictionary(r"C:/lab5/initial.kd")
        print("Loading from: C:/lab5/initial.kd...\n")

        new_block = {'л': {'lackey ': ['menial', 'retainer', 'servant', 'slavey', 'steward', 'dependable', 'reliable', 'responsible']}}
        self.cucumber.extend_kyiv_dictionary(new_block)
        print('Extending Kyiv Dictionary with data:', new_block, '\n')

        self.cucumber.save_kyiv_dictionary("C:/lab5/updated dictionary.kd")

        self.presenter.present_saving_dictionary("Kyiv Dictionary (lab 5)", "C:/lab5/updated dictionary.kd", self.cucumber.kyiv_dictionary)


    def execute_lab6_parts_of_speech_in_ukrainian_language(self):
        self.library.save_parts_of_speech("C:/lab6/initial.spch")
        self.presenter.present_saving_dictionary("Parts of Speech in Ukrainian Language (lab 6)", "C:/lab6/initial.spch", self.library.parts_of_speech.dictionary)

        self.library.load_parts_of_speech("C:/lab6/initial.spch")
        print("Loading from: C:/lab6/initial.spch...")


        self.library.rewrite_parts_of_speech("C:/lab6/new.spch", {'дієслово': {'вид': {   "доконаний": ("заробив",)}}})
        print('Rewriting to C:/lab6/initial.spch completelly...\n')

        self.presenter.present_saving_dictionary("New parts of Speech in Ukrainian Language (lab 6)", "C:/lab6/initial.spch", self.library.parts_of_speech.dictionary)

