import pytest
from model.gateway.file_reader_repository import FileReaderRepository

from tests.fixtures.big_data_examples import whole_raw_text

import os.path


def test_fake_read_from_real_world_file():
    r = FileReaderRepository()
    f = open("C:/lab7/Fedorko/thisfilemustnotexistoutsideofunittesting.txt", 'w', encoding="cp1251")
    f.write("Привіт, світе!")
    f.close()
    r.input_filepath = "C:/lab7/Fedorko/thisfilemustnotexistoutsideofunittesting.txt"

    assert r.read() == "Привіт, світе!"

    # tear down
    os.remove("C:/lab7/Fedorko/thisfilemustnotexistoutsideofunittesting.txt")


def test_file_231_is_clean():

    f = FileReaderRepository()

    assert not os.path.isfile(f.working_dir + '231.txt')


def test_raises_exception_if_file_is_not_found():
    r = FileReaderRepository()
    r.working_dir = "E:/this/file/does/not/exist/"
    with pytest.raises(FileNotFoundError):
        r.read()


def test_make_dir():
    if os.path.isdir('C:/lab0removesitselfautomatically/'):
        os.rmdir("C:/lab0removesitselfautomatically/")

    assert not os.path.isdir('C:/lab0removesitselfautomatically/')

    r = FileReaderRepository()

    r.made_working_directory("C:/lab0removesitselfautomatically/")
    assert os.path.isdir('C:/lab0removesitselfautomatically/')

    os.rmdir("C:/lab0removesitselfautomatically/")
