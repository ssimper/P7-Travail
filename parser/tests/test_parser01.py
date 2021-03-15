import unidecode
from program.parser01 import *


def test_ma_fonction_lowerize_est_ok():
	test = Parser()
	result = test.lowerize()
	assert result == "bonjour grandpy, j'espère que tu vas bien." \
	" dis moi je recherche l'adresse du musée du louvres." \
	" sais-tu où cela ce trouve ?"

def test_ma_fonction_decodize_est_ok():
	test = Parser()
	result2 = test.decodize()
	assert result2 == "bonjour grandpy, j'espere que tu vas bien." \
	" dis moi je recherche l'adresse du musee du louvres." \
	" sais-tu ou cela ce trouve ?"

