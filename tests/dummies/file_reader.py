class FileReaderSpy:
    def __init__(self):
        self.was_read_file_from_default_pathname_called = False

    def read_file_from_default_pathname(self):
        self.was_read_file_from_default_pathname_called = True
        return ""


class Dummy: pass


class FileReaderDummy:
    def read(self):
        return "blah bu"
