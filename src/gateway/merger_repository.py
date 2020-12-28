import nltk
from gateway.file_reader_repository import FileReaderRepository


def append_by_ref_ukrainian_letter_or_replace_with_whitespace(mutable_sentence_by_ref, letter):
    if letter in "АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЮюЯяicICeEoOpPkKHxXMTaA":
        mutable_sentence_by_ref.append(letter)
    else:
        mutable_sentence_by_ref.append(' ')


def merge_two_words(clean_word, second_word):
    return set(clean_word) | set(second_word)


class CleanAndSplitTextRepository:
    def __init__(self):
        self.sentences_list = []

    def split_to_words(self, sentence_with_punctuation):
        return tuple(
            filter(lambda w: w,
                   map(self.__clean_from_punctuation_marks,
                       sentence_with_punctuation.split())))

    @staticmethod
    def __clean_from_punctuation_marks(word):
        clean_word = list()
        return "".join(
            [char
             for char in word
             if char in "АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЮюЯяicICeEoOpPkKHxXMTaA"
             ]
        )

    def append_letters_as_sentence_if_not_empty(self, container_of_letters_with_white_space):
        if container_of_letters_with_white_space:
            self.sentences_list.append("".join(container_of_letters_with_white_space))

    def split_to_clean_sentences(self, text):
        self.sentences_list = []
        sentence = []
        for letter in text:
            if letter in {'.', '?', '!'}:
                self.append_letters_as_sentence_if_not_empty(sentence)
                sentence = []
            else:
                append_by_ref_ukrainian_letter_or_replace_with_whitespace(sentence, letter)

        self.append_letters_as_sentence_if_not_empty(sentence)


class CleanerAndMergerAndReaderRepository(FileReaderRepository, CleanAndSplitTextRepository):
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
            self.split_to_words(first_sentence),
            self.split_to_words(second_sentence))

    def merge_pairs_of_sentences_in_text(self, text_with_punctuation):
        sentences = text_with_punctuation.split('.', 1)

        return self.merge_two_sentences(
            sentences[0],
            "".join([ukrainian_letter for ukrainian_letter in sentences[1] if ukrainian_letter not in 'V_']))

    def pair_and_merge_sentences(self):
        list_of_sets_of_letters = self.merge_two_sentences(self.sentences_list[0], self.sentences_list[1])
        self.merged_sentences = (list_of_sets_of_letters,
                                 self.sentences_list[2])

