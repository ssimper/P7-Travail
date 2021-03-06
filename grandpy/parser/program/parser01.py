import unidecode
import string
import json
import re

class Parser:
	"""Classe chargée de passer en minuscule, retirer
	- les accents
	- l'accentuation
	- la ponctuation
	convertir la question en liste de mots et enfin de
	nettoyer cette liste de ses stop-words"""

	def __init__(self, sentence):
		
		self.sentence = sentence
		

	def lowerize(self):
		# On passe en minuscule
		self.sentence = self.sentence.lower()
		return self.sentence


	def decodize(self):
		# On retire l'accentuation
		self.sentence = unidecode.unidecode(self.sentence)
		return self.sentence


	def remove_ponc(self):
		# On retire la ponctuation
		punctuation = '''!?-.,';'''
		unpuct_sentence = ""
		for char in self.sentence:
			if char not in punctuation:
				unpuct_sentence += char
		self.sentence = unpuct_sentence
		return self.sentence


	def to_list(self):
		# On place les mots dans une liste delimitée par les characères
		# ' (\') et les espaces (\s)
		#self.sentence = re.split('\'|\s', self.sentence)
		self.sentence = re.split('\'|\-|\s', self.sentence)
		#self.sentence = self.sentence.split(' ')
		# On nettoie la liste des éléments vides (espaces)
		for element in self.sentence:
			[self.sentence.remove(element) for element in self.sentence if element == '']
		return self.sentence


	def check_stop_words(self):
		# On nettoie la liste des stop-words
		with open("grandpy/parser/program/fr.json", "r") as read_file:
			stop_words_list = json.load(read_file)
		for word in stop_words_list:
			#word = unidecode.unidecode(word)
			[self.sentence.remove(element) for element in self.sentence if element == word]
		self.sentence = " ".join(self.sentence)
		return self.sentence
	

def main():
	phrase = "Bonjour GrandPy, j'espère que tu vas bien." \
		" Dis moi je recherche l'adresse du Musée du Louvres." \
		" Sais-tu où cela ce trouve ?"
	test = Parser(phrase)
	test.lowerize()
	print(
		"Tout en minuscules :\n", test.sentence)
	print("--------------------")
	test.decodize()
	print(
		"Tout sans accentuation :\n", test.sentence)
	print("--------------------")
	test.remove_ponc()
	print(
		"Tout sans ponctuation :\n", test.sentence)
	print("--------------------")
	test.to_list()
	print("La liste :\n", test.sentence)
	print("--------------------")
	test.check_stop_words()
	print("La liste nettoyée :\n", test.sentence)

if __name__ == "__main__":
    main()
