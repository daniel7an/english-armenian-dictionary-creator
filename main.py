from PyDictionary import PyDictionary
from googletrans import Translator
from write_csv import convert_to_csv

words_path = 'words.txt'
words = []

with open(words_path) as f:
    words = [line.rstrip('\n') for line in f]

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
            spec_meaning = meaning[t][0].replace('"', "")
            if types.index(t) == len(types) - 1:
                meaning_txt += t + ' - ' + spec_meaning
            else:
                meaning_txt += t + ' - ' + spec_meaning + ', '
        rows.append([word, meaning_txt, translation])
    return rows

if __name__ == '__main__':
    rows = process(words)
    convert_to_csv(rows)
    