import pytest
from model.interactor import UserStory

from tests.dummies.presenter_dummies import PresenterDummy


class FileReaderSpy:
    def __init__(self):
        self.was_read_file_from_default_pathname_called = False

    def read(self):
        self.was_read_file_from_default_pathname_called = True
        return ""


@pytest.fixture
def uc() -> UserStory:
    return UserStory(PresenterDummy(), FileReaderSpy(), Replacer())


def test_user_story_reads_data_from_file_reader():
    fr = FileReaderSpy()
    assert not fr.was_read_file_from_default_pathname_called
    uc = UserStory(PresenterDummy(), fr, None)
    uc.modify_sentences_in_text()
    assert fr.was_read_file_from_default_pathname_called