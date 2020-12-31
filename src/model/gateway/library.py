import shelve

from src.entity_part_of_speech.language_interactor import UkrainianLanguageInteractor


class Library:
    def __init__(self, parts_of_speech: UkrainianLanguageInteractor):
        self.parts_of_speech = parts_of_speech

    def save_parts_of_speech(self, path):
        db = shelve.open(path)  # Відкриваємо файл
        # Зберігаємо список
        db["language"] = self.parts_of_speech.dictionary
            # Зберігаємо кортеж
        # Вивід значень
        db.close()

    def load_parts_of_speech(self, path):
        database = shelve.open(path, flag="r")
        try:
            self.parts_of_speech = UkrainianLanguageInteractor(database['language'])
        finally:
            database.close()

    def rewrite_parts_of_speech(self, path, simple_dict):
        database = shelve.open(path, flag="n")
        database.update(language=simple_dict)
        self.parts_of_speech = UkrainianLanguageInteractor(database['language'])
        database.close()

    def print(self):
        print(self.parts_of_speech)