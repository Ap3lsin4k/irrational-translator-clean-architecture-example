import pytest
from model.gateway.file_reader_repository import FileReaderRepository

from tests.fixtures.big_data_examples import whole_raw_text

import os.path


def test_fake_read_from_real_world_file():
    r = FileReaderRepository()
    res = r.read()
    assert res[0] == whole_raw_text[0]
    assert res[1] == whole_raw_text[1]
    assert len(res) == len(whole_raw_text)


def test_file_231_is_clean():

    f = FileReaderRepository()

    assert not os.path.isfile(f.working_dir + '231.txt')



def test_raises_exception_if_file_is_not_found():
    r = FileReaderRepository()
    r.working_dir = "E:/this/file/does/not/exist/"
    with pytest.raises(FileNotFoundError):
        r.read()