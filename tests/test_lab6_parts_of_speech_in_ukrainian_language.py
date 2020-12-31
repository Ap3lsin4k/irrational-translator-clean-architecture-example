from model.gateway.library import Library


def test_nothing():
    lib = Library(PartsOfSpeech)
    lib.save_parts_of_speech()
