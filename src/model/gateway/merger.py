from src.model.gateway.clean_and_split_text_repository import CleanAndSplitTextRepository


def merge_two_words(clean_word, second_word):
    return set(clean_word) | set(second_word)


class MergerService():
    def __init__(self):
        self.merged_sentences = []

    def split_text_to_sentences_and_merge_them(self, text_with_punctuation):
        clean_and_split_repo = CleanAndSplitTextRepository()
        clean_and_split_repo.split_to_clean_sentences(text_with_punctuation)
        self.pair_sentences(clean_and_split_repo.sentences_list)
        return self.merged_sentences

    def pair_sentences(self, sentences_list):
        self.merged_sentences.clear()

        for i in range(1, len(sentences_list), 2):
            self.merge_pair_of_sentences_and_save(sentences_list, i - 1, i)

        index = len(sentences_list) - 1
        if index % 2 == 0:
            self.merge_pair_of_sentences_and_save(sentences_list, index, index)

    def merge_pair_of_sentences_and_save(self, sentences_list, index_left_sentence, index_right_sentence):
        self.merged_sentences.append(
            self.merge_two_sentences(sentences_list[index_left_sentence], sentences_list[index_right_sentence]))

    @staticmethod
    def merge_two_sentences(first_sentence, second_sentence):
        return MergerService.merge_two_lists_of_words(
            CleanAndSplitTextRepository.split_to_words(first_sentence),
            CleanAndSplitTextRepository.split_to_words(second_sentence))

    @staticmethod
    def merge_two_lists_of_words(words1, words2):
        merged_words_vector = []

        for i in range(max(len(words1), len(words2))):
            word1 = words1[i] if len(words1) > i else ""
            word2 = words2[i] if len(words2) > i else ""
            merged_words_vector.append(merge_two_words(word1, word2))

        return merged_words_vector
