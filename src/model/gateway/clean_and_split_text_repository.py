def append_by_ref_ukrainian_letter_or_replace_with_whitespace(mutable_sentence_by_ref, letter):
    if letter in "АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЮюЯяicICeEoOpPkKHxXMTaA":
        mutable_sentence_by_ref.append(letter)
    else:
        mutable_sentence_by_ref.append(' ')


class CleanAndSplitTextRepository:
    def __init__(self):
        self.sentences_list = []

    @staticmethod
    def split_to_words(sentence_with_punctuation):
        return tuple(
            filter(lambda w: w,
                   map(CleanAndSplitTextRepository.clean_from_punctuation_marks,
                       sentence_with_punctuation.split())))

    @staticmethod
    def clean_from_punctuation_marks(word):
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
