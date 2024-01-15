from translate import Translator

translator = Translator(to_lang="ja")
try:
    with open('random_file_for_translator_exercise.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(text)
        print(translation)
except FileNotFoundError as err:
    print('check your file path')

