class KyivDictionary(dict):
    def __init__(self):
        super().__init__()

        # згенерувати список з ключами - українські літери, значення - пусті словники
        # for i in range(1072, 1072 + 33):
        #    self.update({chr(i): dict()})

        self.update({
            'а': {'vulnerable': ["endangered", "exposed", "liable", "open", "sensitive"]},
            'б': {'ulterior': ["further", "future"]},
            'в': {'vulgar': ['coarse', 'gross', 'earthy'],
                  'vacuum': ['brush', 'comb', 'dry-clean', 'blackness', 'nothingness']},

            'г': {'catch': ['bag', 'capture', 'corral', 'get', 'glom', 'grab', 'snare', 'snatch', 'trap']},
            'д': {'cat': ['feline', 'kitty', 'moggy']},

            'е': {'happy': ['fluky', 'fortuitous', 'fortunate', 'heaven-sent', 'lucky', 'providential']},
            'ж': {'grateful': ['appreciative', 'appreciatory', 'glad', 'obliged', 'thankful']},

            'з': {'grade': ['chapter', 'cut', 'degree', 'inch', 'notch']},

            'и': {'gradient': ['cant', 'diagonal', 'inclination', 'incline']},
            'й': {'solid': ['commonsense', 'commonsensible', 'commonsensical', 'firm', 'good']},
            'к': {'solid': ['calculable', 'dependable', 'reliable', 'responsible']},
                #'л': {}, 'м': {}, 'н': {}, 'о': {},
                # 'п': {}, 'р': {}, 'с': {}, 'т': {}, 'у': {}, 'ф': {}, 'х': {}, 'ц': {}, 'ч': {}, 'ш': {}, 'ь': {},
            # 'э': {},
        })

        self.similar_words = list()
        self.synonyms = list()
    import math
    math.factorial(4)

    def words_that_begin_with(self, prefix):
        self.similar_words = list()
        self.synonyms = list()
        for key in self:
            for foreign_word in self[key]:
                if len(prefix) < len(foreign_word):
                    if prefix in foreign_word[:len(prefix)]:
                        self.similar_words.append(foreign_word)
                elif prefix == foreign_word:
                    self.synonyms.append(self[key][foreign_word])

                    # відкоментуйте, щоб включити слова з точним співпадінням
                    # до переліку слів, що починаються на введене
                    # self.similar_words.append(foreign_word)

