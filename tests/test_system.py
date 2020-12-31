from gateway.replace_service import Replacer
from src import UserStory, Presenter, FileReaderRepository


def test_whole_system_makes_231file():
    interactor = UserStory(Presenter(FileReaderRepository()), FileReaderRepository(), Replacer())
    interactor.modify_sentences_in_text()
    interactor.execute_replacer()