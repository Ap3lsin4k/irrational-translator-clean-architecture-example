class View:
    last_message = ""

    def print(self, *args, sep=' ', end='\n', file=None):
        if file is not None:
            raise NotImplementedError

        text = sep.join(map(str, args)) + end
