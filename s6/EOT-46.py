def foraVocals(cadena):	
	r = ""
	vocals = "aeiouAEIOU"
	for char in cadena:
		if char not in vocals:
			r += char
	return r

def modificaCadena(cadena):
	count = len(cadena)
	i = 0
	r = ""
	a = "bogeria"
	while i < count:
		r += cadena[i:i+3] + a
		print "(", i,")", r
		i += 3
	return r

cadena = raw_input("Introdueix una cadena: ")
cadena = foraVocals(cadena)
print "El primer pas genera:", cadena, "\n"

start = input("Introdueix el primer index de la subcadena: ")
end = input("Introdueix el segon index de la subcadena: ")
cadena = cadena[start:end]
print "El segon pas genera:", cadena



print "La teva cadena resultant es:", modificaCadena(cadena)
