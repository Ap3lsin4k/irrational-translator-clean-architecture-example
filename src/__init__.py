#__init__.py
from src.model.gateway.file_reader_repository import FileReaderRepository
from src.model.gateway.merger import MergerService
from src.model.gateway.replace_service import Replacer
from src.model.interactor import UserStory
from src.presentation import Presenter

if __name__ == '__main__':
    interactor = UserStory(Presenter(FileReaderRepository()), FileReaderRepository(), Replacer(), MergerService())
    interactor.make_directories()
    interactor.execute_lab5_kyiv_dictionary()
    interactor.execute_lab6_parts_of_speech_in_ukrainian_language()
    interactor.modify_sentences_in_text()
    interactor.execute_replacer()