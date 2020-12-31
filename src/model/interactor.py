from model.gateway.clean_and_split_text_repository import CleanAndSplitTextRepository
from model.gateway.merger import MergerRepository


class UserStory:
    def __init__(self, presenter, text_reader, replacer):
        self.presenter = presenter
        self.text_reader = text_reader
        self.replacer = replacer
        self.merger_service = MergerRepository()

    def modify_sentences_in_text(self):
        self.merger_service.split_text_to_sentences_and_merge_them(self.text_reader.read())
        self.presenter.present(self.merger_service.merged_sentences)

    def execute_replacer(self):
        self.replacer.replace_vowels_with_consonant(self.text_reader.read())


