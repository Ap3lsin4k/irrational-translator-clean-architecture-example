from gateway.clean_and_split_text_repository import CleanAndSplitTextRepository
from gateway.file_reader_repository import FileReaderRepository




def merge_two_words(clean_word, second_word):
    return set(clean_word) | set(second_word)


class MergerRepository(FileReaderRepository):
    def __init__(self):
        self.merged_sentences = []

    @staticmethod
    def merge_two_lists_of_words(words1, words2):
        merged_words_vector = []

        for i in range(max(len(words1), len(words2))):
            word1 = words1[i] if len(words1) > i else ""
            word2 = words2[i] if len(words2) > i else ""
            merged_words_vector.append(merge_two_words(word1, word2))

        return merged_words_vector

    def merge_two_sentences(self, first_sentence, second_sentence):
        return self.merge_two_lists_of_words(
            CleanAndSplitTextRepository.split_to_words(first_sentence),
            CleanAndSplitTextRepository.split_to_words(second_sentence))

    def merge_pairs_of_sentences_in_text(self, text_with_punctuation):
        sentences = text_with_punctuation.split('.', 1)

        return self.merge_two_sentences(
            sentences[0],
            "".join([ukrainian_letter for ukrainian_letter in sentences[1] if ukrainian_letter not in 'V_']))

    def pair_and_merge_sentences(self, sentences_list):
        list_of_sets_of_letters = self.merge_two_sentences(sentences_list[0], sentences_list[1])
        second = self.merge_two_sentences(sentences_list[2], sentences_list[2])

        self.merged_sentences = (list_of_sets_of_letters, second)
