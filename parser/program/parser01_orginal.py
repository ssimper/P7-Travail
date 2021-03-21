import unidecode
import string
import json

class Parser:
	"""Classe chargée de passer en minuscule, retirer
	- les accents
	- l'accentuation
	- la ponctuation
	convertir la question en liste de mots et enfin de
	nettoyer cette liste de ses stop-words"""

	def __init__(self):
		
		self.question = "Bonjour GrandPy, j'espère que tu vas bien." \
		" Dis moi je recherche l'adresse du Musée du Louvres." \
		" Sais-tu où cela ce trouve ?"



	def lowerize(self):
		# On passe en minuscule
		result = self.question.lower()
		self.result = result
		return result


	def decodize(self):
		# On retire l'accentuation
		result2 = unidecode.unidecode(self.result)
		self.result2 = result2
		return result2


	def remove_ponc(self):
		# On retire la ponctuation
		result3 = self.result2.translate(
			str.maketrans('', '', string.punctuation)
			)
		self.result3 = result3
		return result3

	def to_list(self):
		# On place les mots dans une liste
		result4 = self.result3.split(' ')
		self.result4 = result4
		return result4


	def check_stop_words(self):
		# On nettoie la liste des stop-words
		with open("fr.json", "r") as read_file:
			stop_words_list = json.load(read_file)
		for word in stop_words_list:
			[self.result4.remove(element) for element in self.result4 if element == word]
		self.result5 = self.result4
		result5 = self.result5
		return result5


def main():
	test = Parser()
	test.lowerize()
	print(
		"Tout en minuscules :\n", test.result)
	print("--------------------")
	test.decodize()
	print(
		"Tout sans accentuation :\n", test.result2)
	print("--------------------")
	test.remove_ponc()
	print(
		"Tout sans ponctuation :\n", test.result3)
	print("--------------------")
	test.to_list()
	print("La liste :\n", test.result4)
	print("--------------------")
	test.check_stop_words()
	print("La liste nettoyée :\n", test.result5)

if __name__ == "__main__":
    main()
