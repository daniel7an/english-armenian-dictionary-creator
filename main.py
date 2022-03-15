from PyDictionary import PyDictionary
from googletrans import Translator

dictionary = PyDictionary()
translator = Translator()

word = input('Please, type the word: ')


print('meaning: ', dictionary.meaning(word))
print('transtaltion: ', translator.translate(word, dest='hy'))
