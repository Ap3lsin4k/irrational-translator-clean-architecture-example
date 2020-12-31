import pickle

from src.model.gateway.cucumber import Cucumber
from src.other.kyiv_dictionary_entity import KyivDictionary
from src import UserStory, MergerRepository

import os

from tests.dummies.file_reader import FileReaderRepositoryDummy


def test_nothing():
    uc = UserStory(None, FileReaderRepositoryDummy(), None, MergerRepository())
    if os.path.exists("E:/lab5/initial.kd"):
        os.remove("E:/lab5/initial.kd")

    kd = KyivDictionary()
   # f = open("E:/lab5/")

    uc.make_directories()
    cucumber = Cucumber(kd)
    cucumber.save_kyiv_dictionary("E:/lab5/initial.kd")
    cucumber.load_kyiv_dictionary_from_default_path(r"E:/lab5/initial.kd")

    assert cucumber.kyiv_dictionary == kd
    cucumber.extend_kyiv_dictionary({'л':  {'lackey ': ['menial', 'retainer', 'servant', 'slavey', 'steward', 'dependable', 'reliable', 'responsible']}})
    cucumber.save_kyiv_dictionary("E:/lab5/updated dictionary.kd")

    assert len(cucumber.kyiv_dictionary) > len(kd)

    temp = cucumber.kyiv_dictionary
    cucumber.kyiv_dictionary = None
    assert temp
    cucumber.load_kyiv_dictionary_from_default_path(r"E:/lab5/updated dictionary.kd")
    assert cucumber.kyiv_dictionary == temp
