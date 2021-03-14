import unidecode
import string

class Parser:


	def __init__(self):
		
		self.question = "Bonjour GrandPy, j'espère que tu vas bien." \
		" Dis moi je recherche l'adresse du Musée du Louvres." \
		" Sais-tu où cela ce trouve ?"



	def lowerize(self):
		result = self.question.lower()
		self.result = result
		return result


	def decodize(self):
		result2 = unidecode.unidecode(self.result)
		self.result2 = result2
		return result2


	def remove_ponc(self):
		result3 = self.result2.translate(
			str.maketrans('', '', string.punctuation)
			)
		self.result3 = result3
		return result3

	def to_list(self):
		result4 = self.result3.split(' ')
		self.result4 = result4
		return result4


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

if __name__ == "__main__":
    main()
