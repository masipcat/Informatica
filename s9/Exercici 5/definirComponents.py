from dbManager import *
import sys


if len(sys.argv) > 1:
	filename = sys.argv[1]
	contingut = obreFitxer(filename)
	contingut += "\nMitjana de components: " + str(mitjanaComponents(contingut))
	desaFitxer(filename, contingut)
else:
	print "Defineix els components: "
	components = llegirComponents()
	desaFitxer("components.txt", components)
