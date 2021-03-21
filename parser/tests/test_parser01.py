import unidecode
import json
from program.parser01 import *


def test_ma_fonction_lowerize_est_ok():
	test = Parser("Je vais aux Champs Elysées, à la Défense et à la Tour eiffel.")
	result = test.lowerize()
	assert result == "je vais aux champs elysées, à la défense et à la tour eiffel."


def test_ma_fonction_decodize_est_ok():
	test = Parser("Les élèves sont déçus.")
	result = test.decodize()
	assert result == "Les eleves sont decus."


def test_ma_fonction_remove_ponc_est_ok():
	test = Parser("Des figues, des bananes; des poires !")
	result = test.remove_ponc()
	assert result == "Des figues des bananes des poires "


def test_ma_fonction_to_list_est_ok():
	test = Parser("What is your favorite color ?")
	result = test.to_list()
	assert result == ['What', 'is', 'your', 'favorite', 'color', '?']


def test_ma_fonction_check_stop_words_est_ok():
	test = Parser(['desormais', 'il', 'allait', 'manger', 'rarement', 'des', 'pizzas.'])
	result = test.check_stop_words()
	assert result == ['allait', 'manger', 'pizzas.']
