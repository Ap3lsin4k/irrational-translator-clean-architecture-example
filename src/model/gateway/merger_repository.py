def merge_two_words(clean_word, second_word):
    return set(clean_word) | set(second_word)


class MergerRepository():
    def __init__(self):
        pass
    
    @staticmethod
    def merge_two_lists_of_words(words1, words2):
        merged_words_vector = []

        for i in range(max(len(words1), len(words2))):
            word1 = words1[i] if len(words1) > i else ""
            word2 = words2[i] if len(words2) > i else ""
            merged_words_vector.append(merge_two_words(word1, word2))

        return merged_words_vector