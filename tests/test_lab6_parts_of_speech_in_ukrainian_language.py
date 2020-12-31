import os

from src.entity_part_of_speech.presentation.ua_lang_controller import ua_lang

from src.model.gateway.library import Library


def test_shelve():

    if os.path.exists("E:/lab5/initial.spch"):
        os.remove("E:/lab5/initial.spch")

    parts_of_speech = ua_lang
    lib = Library(parts_of_speech)
    lib.save_parts_of_speech("E:/lab6/initial.spch")
    lib.load_parts_of_speech("E:/lab6/initial.spch")
    assert lib.parts_of_speech.dictionary == parts_of_speech.dictionary
    lib.rewrite_parts_of_speech("E:/lab6/initial.spch", {
        'дієслово': {
            'вид': {
                "доконаний":
                    ("заробив",)}}})
    assert lib.parts_of_speech.dictionary == {
'дієслово': {
'вид': {
"доконаний":
    ("заробив",)}}}
    #lib.rewrite_parts_of_speech()
    #assert os.path.exists("E:/lab5/initial.spch")

#    lib.load_parts_of_speech("E:/lab6/initial.spch")

 #   assert lib.parts_of_speech == ua_lang

   # lib.update({'л':  {'lackey ': ['menial', 'retainer', 'servant', 'slavey', 'steward', 'dependable', 'reliable', 'responsible']}})
   # lib.save_kyiv_dictionary("E:/lab5/updated dictionary.kd")

    #assert len(cucumber.kyiv_dictionary) > len(kd)

#    temp = cucumber.kyiv_dictionary
#    cucumber.kyiv_dictionary = None
#    assert temp
#    cucumber.load_kyiv_dictionary(r"E:/lab5/updated dictionary.kd")
#   assert cucumber.kyiv_dictionary == temp

