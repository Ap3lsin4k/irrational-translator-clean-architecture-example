from model.gateway.clean_and_split_text_repository import CleanAndSplitTextRepository
from model.gateway.merger_repository import MergerRepository


class UserStory:
    @staticmethod
    def merge_two_sentences(first_sentence, second_sentence):
        return MergerRepository.merge_two_lists_of_words(
            CleanAndSplitTextRepository.split_to_words(first_sentence),
            CleanAndSplitTextRepository.split_to_words(second_sentence))

    @staticmethod
    def split_text_to_sentences_and_merge_them(text_with_punctuation):
        clean_and_split_repo = CleanAndSplitTextRepository()
        clean_and_split_repo.split_to_clean_sentences(text_with_punctuation)

        return UserStory.merge_two_sentences(
            clean_and_split_repo.sentences_list[0],
            "".join([ukrainian_letter for ukrainian_letter in clean_and_split_repo.sentences_list[1] if ukrainian_letter not in 'V_']))