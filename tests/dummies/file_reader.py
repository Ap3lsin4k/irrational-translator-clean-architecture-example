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


class FileReaderRepositoryDummy():
    working_dir = 'C:/lab7/Fedorko/'
    input_filepath = working_dir + '23.txt'

    def __init__(self):pass

    def made_working_directory(self, dir_path): pass

    def read(self):
        pass
    def read_file_from_default_path(self):
        pass

    def print(self, *args, sep=' ', end='\n', file=None):
        pass

    def __write(self, text): pass