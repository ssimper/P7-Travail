import unidecode
from program.parser01 import lowerize



def test_ma_fonction_lowerize_est_ok():
	result = lowerize()
	assert result == "bonjour grandpy, j'espère que tu vas bien. dis moi je recherche l'adresse du musée du louvres. sais-tu où cela ce trouve ?"