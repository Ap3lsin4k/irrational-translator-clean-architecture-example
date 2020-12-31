class PresenterDummy():
    def present_sentence(self, args):
        pass

    def present(self, args): pass


class PresenterSpy:
    def __init__(self, view): pass

    last_message = None
    last_error_message = None

    def present(self, args):
        self.last_message = str(args)

    def present_sentence(self, args): pass

    def present_error(self, printable):
        self.last_error_message = printable