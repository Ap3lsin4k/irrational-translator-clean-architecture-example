from model.gateway.replace_service import Replacer
from src import UserStory, Presenter, FileReaderRepository

from tests.fixtures.big_data_examples import whole_raw_text


def test_whole_system():
    interactor = UserStory(Presenter(FileReaderRepository()), FileReaderRepository(), Replacer())
    interactor.make_directories()
    interactor.execute_lab5_kyiv_dictionary()
    interactor.execute_lab6_parts_of_speech_in_ukrainian_language()
    interactor.modify_sentences_in_text()
    interactor.execute_replacer()


def test_fake_read_from_real_world_file():
    r = FileReaderRepository()
    res = r.read()
    assert res[0] == whole_raw_text[0]
    assert res[1] == whole_raw_text[1]
    assert len(res) == len(whole_raw_text)

