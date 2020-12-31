import io
import os


class FileReaderRepository:
    working_dir = 'C:/lab7/Fedorko/'

    def __init__(self):
        if os.path.isfile(self.working_dir+'231.txt'):
            os.remove(self.working_dir+'231.txt')

    def read(self):
        if os.path.isdir('C:/lab7/'):
            if os.path.isdir(self.working_dir):
                if os.path.isfile(self.working_dir+'23.txt'):
                    return self.read_file_from_default_path()
                else:
                    raise FileNotFoundError("Error: C:/lab7/Fedorko/23.txt must be created to read the input text")
            else:
                raise FileNotFoundError("Error: C:/lab7/Fedorko/ directory must be created")
        else:
            raise FileNotFoundError("Error: C:/lab7/ directory must be created")
        # TODO create them if they do not exist

    def read_file_from_default_path(self):
        with open(self.working_dir + '23.txt', mode='r', encoding="cp1251") as f:
            return f.read()

    def print(self, *args, sep=' ', end='\n', file=None):
        if file is not None:
            raise NotImplementedError

        text = sep.join(map(str, args)) + end

        self.__write(text)

    def __write(self, text):
        with open(self.working_dir + '231.txt', "a", encoding="cp1251") as f:
            f.write(text)
# TODO a check whether directory or file exist and make nice output