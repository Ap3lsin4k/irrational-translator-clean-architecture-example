import pickle

from other.kyiv_dictionary_entity import KyivDictionary


class Cucumber:

    def __init__(self, kyiv_dictionary):
        self.kyiv_dictionary = kyiv_dictionary

    def save_kyiv_dictionary(self, path):
        f = open(path, "wb")
        pickle.dump(self.kyiv_dictionary, f)
        f.close()

    def load_kyiv_dictionary_from_default_path(self, path):
        f = open(path, "rb")
        self.kyiv_dictionary = pickle.load(f)
        f.close()

    def extend_kyiv_dictionary(self, param):
        self.kyiv_dictionary.update(param)