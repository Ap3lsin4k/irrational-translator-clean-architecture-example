from model.gateway.file_reader_repository import FileReaderRepository

from tests.fixtures.big_data_examples import whole_raw_text


def test_read():
    r = FileReaderRepository()
    res = r.read_file_from_default_pathname()
    assert len(res) == len(whole_raw_text)