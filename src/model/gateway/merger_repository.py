def merge_two_words(clean_word, second_word):
    return set(clean_word) | set(second_word)


class MergerRepository():
    def __init__(self, interactor_callback_hell):
        self.merged_sentences = []
        self.interactor_callback_hell = interactor_callback_hell

    @staticmethod
    def merge_two_lists_of_words(words1, words2):
        merged_words_vector = []

        for i in range(max(len(words1), len(words2))):
            word1 = words1[i] if len(words1) > i else ""
            word2 = words2[i] if len(words2) > i else ""
            merged_words_vector.append(merge_two_words(word1, word2))

        return merged_words_vector

    def pair_and_merge_sentences(self, sentences_list):
        self.merged_sentences.clear()

        for i in range(1, len(sentences_list), 2):
            self.__merge(sentences_list, i - 1, i)

        index = len(sentences_list) - 1
        if index % 2 == 0:
            self.__merge(sentences_list, index, index)

    def __merge(self, sentences_list, index_left_sentence, index_right_sentence):
        self.merged_sentences.append(
            self.interactor_callback_hell.merge_two_sentences(sentences_list[index_left_sentence], sentences_list[index_right_sentence]))
# TODO remove interactor