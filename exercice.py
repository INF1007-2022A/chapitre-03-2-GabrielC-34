#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	return (voltage**2)/resistance

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	if(v1[0]*v2[0] + v1[1]*v2[1]) == 0:
		estOrthogonal = True
	else:
		estOrthogonal = False
	return estOrthogonal

def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	nbrValues = 0
	addValue = 0
	for v in values:
		if v >= 0:
			addValue+=v
			nbrValues+=1
	return addValue/nbrValues



def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	twenties, tens, fives, ones = 0,0,0,0
	while value != 0:
		if value >= 20:
			value-=20
			twenties+=1
		elif value >= 10:
			value -= 10
			tens += 1
		elif value >= 5:
			value -= 5
			fives += 1
		elif value >= 1:
			value -= 1
			ones += 1

	return (twenties, tens, fives, ones);

def format_base(value, base, digit_letters):
	# Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres<
	# `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
	result = ""
	abs_value = abs(value)
	while abs_value != 0:
		nbrOfFactor = int(abs_value % base) #Vérifie combien de fois la nouvelle base rentre dans le nombre
		result += digit_letters[nbrOfFactor] #Ajoute la lettre/le chiffre correspondant au résultat
		abs_value = abs_value//base #Réajuste la valeur du nombre
	if value < 0:
		# TODO: Ne pas oublier d'ajouter '-' devant pour les nombres négatifs.
		result+='-'
	return result[::-1] #Inverse la string


if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
	print(format_base(-42, 16, "0123456789ABCDEF"))
