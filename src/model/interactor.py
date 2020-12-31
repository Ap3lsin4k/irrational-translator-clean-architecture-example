from model.gateway.clean_and_split_text_repository import CleanAndSplitTextRepository
from model.gateway.merger_repository import MergerRepository


class UserStory:
    def __init__(self, presenter, text_reader, replacer):
        self.merged_sentences = []
        self.presenter = presenter
        self.text_reader = text_reader
        self.replacer = replacer

    def modify_sentences_in_text(self):
        self.split_text_to_sentences_and_merge_them(self.text_reader.read())
        self.presenter.present(self.merged_sentences)

    def split_text_to_sentences_and_merge_them(self, text_with_punctuation):
        clean_and_split_repo = CleanAndSplitTextRepository()
        clean_and_split_repo.split_to_clean_sentences(text_with_punctuation)
        self.pair_and_merge_sentences(clean_and_split_repo.sentences_list)
        return self.merged_sentences

    def pair_and_merge_sentences(self, sentences_list):
        self.merged_sentences.clear()

        for i in range(1, len(sentences_list), 2):
            self.__merge(sentences_list, i - 1, i)

        index = len(sentences_list) - 1
        if index % 2 == 0:
            self.__merge(sentences_list, index, index)

    def __merge(self, sentences_list, index_left_sentence, index_right_sentence):
        self.merged_sentences.append(
            self.merge_two_sentences(sentences_list[index_left_sentence], sentences_list[index_right_sentence]))

    @staticmethod
    def merge_two_sentences(first_sentence, second_sentence):
        return MergerRepository.merge_two_lists_of_words(
            CleanAndSplitTextRepository.split_to_words(first_sentence),
            CleanAndSplitTextRepository.split_to_words(second_sentence))

    def execute_replacer(self):
        self.replacer.replace_vowels_with_consonant(self.text_reader.read())
        pass

