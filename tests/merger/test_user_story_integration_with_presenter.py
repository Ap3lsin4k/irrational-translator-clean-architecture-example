from model.interactor import UserStory

from tests.dummies.file_reader import FileReaderDummy
from tests.dummies.presenter_dummies import PresenterSpy


def test_user_story_gives_info_to_presenter():
    presenter = PresenterSpy(None)
    uc = UserStory(presenter, FileReaderDummy(), None)
    assert not presenter.last_message
    uc.modify_sentences_in_text()
    assert presenter.last_message
