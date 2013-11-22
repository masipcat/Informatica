from funcionsMat import *
import sys

def desaFitxer(nom, contingut):
	f = open(nom, "w")
	f.write(contingut)
	f.close()
	return True

def llegeixFitxer(nom):
	f = open(nom)
	content = f.read()
	f.close()
	return content

def init():
	args = sys.argv[1:]
	if len(args) == 0: # Es demana una matriu
		matrix = decodeMatriu(llegeixMatriu(3,3))
		desaFitxer("mat.txt", matrix)
	else: # Obrir matriu
		matriu = encodeMatriu(llegeixFitxer(args[0]))
		mostraMatriu(matriu)

init()
