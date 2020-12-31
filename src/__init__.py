#__init__.py
import builtins

from model.gateway.file_reader_repository import FileReaderRepository
from model.interactor import UserStory
from presentation import Presenter

if __name__ == '__main__':
    interactor = UserStory(Presenter(FileReaderRepository()), FileReaderRepository(), Replacer())
    interactor.modify_sentences_in_text()