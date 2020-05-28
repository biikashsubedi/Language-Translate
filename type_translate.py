from translate import Translator
import argparse

args = argparse.ArgumentParser("python3 type_translate.py")

args.add_argument('-ne', '-nepali')
args.add_argument('-ja', '-japanese')
args.add_argument('-es', '-spanish')

options = args.parse_args()

translator= Translator(to_lang="ja")

text = input("Enter To Translate: ")

translation = translator.translate(text)
print(translation)
