# language_interactor.py
from entity_part_of_speech.language_entity import LanguageEntity
from entity_part_of_speech.repositories.correct_typo_repository import CorrectTypo
from entity_part_of_speech.repositories.word_classifier_repository import WordClassifierRepository
from entity_part_of_speech.repositories.word_of_same_category_repository import WordsOfSameCategoryRepository


class UkrainianLanguageInteractor():
    def __init__(self, nested_dictionary):
        self.dictionary = LanguageEntity(nested_dictionary)
        self.__classifier = WordClassifierRepository(self.dictionary)
        self.__words_same_category = WordsOfSameCategoryRepository(self.dictionary)

    # WORD CLASSIFIER
    def classify(self, input_word):
        self.__classifier.for_each_part_of_speech(self.__classifier.make_response_model, input_word)
        return self.__classifier.result

    # SHOW EXAMPLES OF WORDS FOR GIVEN PROPERTY, SHOW CLASS OF WORDS WITH SAME PROPERTY
    def get_examples(self, property_name):
        self.__words_same_category.for_each_part_of_speech(self.__words_same_category.find_words_in_category_of_properties, property_name)
        res = [self.__words_same_category.result, self.__words_same_category.bm]
        return res

    def modify(self, bookmark, old_word, new_word):
        modifiable = list(self.dictionary.get_words_for_property(bookmark))
        index = modifiable.index(old_word)
        modifiable[index] = new_word
        self.dictionary[bookmark.get_part_of_speech()][bookmark.category_name][bookmark.property_name] = tuple(modifiable)

    def update(self, param):
        self.dictionary.update(param)

    def construct_close_matches(self, typo):
        suggestion = set()
        CorrectTypo().get_close_matches(suggestion, self.dictionary, typo)
        return suggestion



