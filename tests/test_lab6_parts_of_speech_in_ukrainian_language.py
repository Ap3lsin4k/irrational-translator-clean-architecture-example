from src.entity_part_of_speech.presentation.ua_lang_controller import ua_lang

from src.model.gateway.library import Library


def test_nothing():
    lib = Library(ua_lang)
    lib.save_parts_of_speech()
