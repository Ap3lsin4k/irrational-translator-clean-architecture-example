import io
import os


class FileReaderRepository:
    working_dir = 'C:/lab7/Fedorko/'
    input_filepath = working_dir + '23.txt'

    def __init__(self):
        if os.path.isfile(self.working_dir + '231.txt'):
            os.remove(self.working_dir + '231.txt')

    def made_working_directory(self, dir_path):
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)
            return True
        return False

    def read(self):
        #        from pathlib import Path
        #        Path(self.working_dir).mkdir(parents=True, exist_ok=True)
        if os.path.isdir('C:/lab7/'):
            if os.path.isdir(self.working_dir):
                if os.path.isfile(self.input_filepath):
                    return self.read_file_from_default_path()
                else:
                    raise FileNotFoundError("Error: please put '23.txt' file with text into C:/lab7/Fedorko/ folder")
            else:
                raise FileNotFoundError("Error: C:/lab7/Fedorko/ directory must be created")
        else:
            raise FileNotFoundError("Error: C:/lab7/ directory must be created")

    def read_file_from_default_path(self):
        with open(self.input_filepath, mode='r', encoding="cp1251") as f:
            return f.read()

    def print(self, *args, sep=' ', end='\n', file=None):
        if file is not None:
            raise NotImplementedError

        text = sep.join(map(str, args)) + end

        self.write(text)

    def write(self, text, path='C:/lab7/Fedorko/231.txt'):
        with open(path, "a", encoding="cp1251") as f:
            f.write(text)
