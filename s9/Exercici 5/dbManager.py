#!/usr/bin/env python
# -*- coding: utf-8 -*

"""
5. Escriviu una funció de nom llegirComponents() tal que, demani a l'usuari per teclat 20 nombres corresponents als codis de fabricació de components electrònics, i per cada codi es demani també el seu preu. El programa ha de guardar codi preu en un fitxer de text de nom components.txt. Escriviu una funció de nom mitjanaComponents() tal que obtingui les dades del fitxer de text anterior, calculi la mitjana de preus dels components i escrigui en la darrera línia del fitxer components.txt la frase: "Mitjana de components:" i el resultat del càlcul anterior. Finalment, creeu un script que utilitzi les funcions anteriors.
"""

def llegirComponents():
	components = ""
	for i in range(20):
		print "---------"
		components += "\n" + raw_input("Component " + str(1+i) + ": ") + "," + raw_input("Preu: ")
	return components[1:]

def mitjanaComponents(components):
	suma_preu = 0.0
	components = components.split("\n")
	for component in components:
		component = component.split(",")
		if len(component) == 2:
			suma_preu += float(component[1])
	return suma_preu / len(components)

def desaFitxer(nom, content):
	f = open(nom, "w")
	f.write(content)
	f.close()

def obreFitxer(fitxer):
	f = open(fitxer)
	content = f.read()
	f.close()
	return content
