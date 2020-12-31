import pytest
from model.interactor import UserStory

from tests.dummies.file_reader import FileReaderDummy


class PresenterSpy:
    def __init__(self, view): pass

    last_message = None
    
    def present(self, args):
        self.last_message = str(args)

    def present_sentence(self, args): pass


def test_user_story_gives_info_to_presenter():
    presenter = PresenterSpy(None)
    uc = UserStory(presenter, FileReaderDummy(), None)
    assert not presenter.last_message
    uc.modify_sentences_in_text()
    assert presenter.last_message
