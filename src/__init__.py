#__init__.py
from src.model.gateway.file_reader_repository import FileReaderRepository
from src.model.gateway.merger import MergerRepository
from src.model.gateway.replace_service import Replacer
from src.model.interactor import UserStory
from src.presentation import Presenter

if __name__ == '__main__':
    interactor = UserStory(Presenter(FileReaderRepository()), FileReaderRepository(), Replacer(), MergerRepository())
    interactor.modify_sentences_in_text()
    interactor.execute_replacer()