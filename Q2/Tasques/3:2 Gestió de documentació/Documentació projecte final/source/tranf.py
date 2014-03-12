#!/usr/bin/python
# -*- coding: utf-8 

"""
============
tranf module
============

Use this module to **scale** images.
"""

# DEV: Felipe Arango

#from utiles import *
#from img import *
#import math, split

# Les funcions htrim() i vtrim() han estat implementades a "split.py"

def scale(src, h):
	"""
	Scale image src taking into account height h preserving ratio aspect

	:param src: image list
	:type src: list
	:param h: new height
	:type h: int
	>>> scale(('RGB', [[(255, 255, 255), (255, 255, 255), (255, 255, 255)], [(255, 255, 255),
	(255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255), (255, 255, 255)]]),2)
	('1', [[(255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255)]])
	>>> scale(('RGB', [[(0, 0, 0), (255, 255, 255), (255, 0, 0)], [(255, 255, 255), (0, 255, 0),
	(255, 255, 255)], [(0, 0, 255), (255, 255, 255), (255, 255, 255)]]),2)
	('1', [[(0, 0, 0), (255, 0, 0)], [(0, 0, 255), (255, 255, 255)]])
	"""

	# Factor d'escalat
	Fh = get_h(src)/float(h)

	# Nova amplada per l'escalada	
	new_w=get_w(src)/float(Fh)
	
	imatge_final=[]
	src_imatge=src[1] #retorna només l'imatge src (senre el "RGB")
	for a in range(int(h)):
		nova_imatge=[]
		for b in range(int(new_w)):
			nova_imatge += (src_imatge[int(math.ceil(a*Fh))][int(math.ceil(b*Fh))],)
		imatge_final+=[nova_imatge]
	return (src[0], imatge_final)
