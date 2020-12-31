import os

from src import FileReaderRepository, UserStory

from tests.dummies.presenter_dummies import PresenterSpy
from tests.dummies.replacer import ReplacerDummy


def test_warns_if_file_does_not_exist():
    presenter = PresenterSpy(None)
    reader = FileReaderRepository()
    uc = UserStory(presenter, reader, ReplacerDummy(), MergerRepository())
    # do not create file
    assert not presenter.last_error_message
    reader.input_filepath = reader.working_dir + "thisfiledefinatellydoesnotexist.txt"
    uc.execute_replacer()
    assert not presenter.last_message
    assert "Error" in "{}".format(presenter.last_error_message)

def test_finds_file_if_exists():
    # setup
    presenter = PresenterSpy(None)
    reader = FileReaderRepository()
    uc = UserStory(presenter, reader, ReplacerDummy(), MergerRepository())
    open("C:/lab7/Fedorko/thisfilemustnotexistoutsideofunittesting.txt", 'w').close()
    reader.input_filepath = "C:/lab7/Fedorko/thisfilemustnotexistoutsideofunittesting.txt"

    assert not presenter.last_error_message
    reader.input_filepath = reader.working_dir + "thisfilemustnotexistoutsideofunittesting.txt"
    uc.execute_replacer()
    assert not presenter.last_error_message

    # tear down
    os.remove("C:/lab7/Fedorko/thisfilemustnotexistoutsideofunittesting.txt")
    #remove file