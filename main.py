from PyDictionary import PyDictionary
from googletrans import Translator
from write_csv import convert_to_csv

words = ['rescue', 'door', 'car', 'big']

dictionary = PyDictionary()
translator = Translator()

def process(words):
    rows = []
    for word in words:
        # defining str variable for meaning
        meaning_txt = ''
        meaning = dictionary.meaning(word)
        translation = translator.translate(word, src='en', dest='hy').text
        types = list(meaning.keys())

        for t in types:
            spec_meaning = meaning[t][0]
            if types.index(t) == len(types) - 1:
                meaning_txt += t + ' - ' + spec_meaning
            else:
                meaning_txt += t + ' - ' + spec_meaning + ', '
        rows.append([word, translation, meaning_txt])
    return rows

if __name__ == '__main__':
    rows = process(words)
    convert_to_csv(rows)