#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
============
imgio module
============

Use this module to work with image files. You can **read**, **write** and **show** image files easly.
"""

# DEV: Adrià Auguets i Felipe Arango

#from img import *
#from PIL import Image

def read_rgb(nomf):
	"""
	Read image as rgb matrix from file. Returns a tuple like (image_matrix, "RGB")

	:param nomf: filename
	:type nomf: str
	"""
	image = Image.open(nomf)
	pix = image.load()
	X, Y = image.size[0], image.size[1]
	data = [[pix[x,y] for x in range(X)] for y in range(Y)]    
	return img(data, 'RGB')


def read_bn(nomf):
	"""
	Read image as bw matrix from file. Returns a image_matrix

	:param nomf: filename
	:type nomf: str
	"""
	image = Image.open(nomf).convert('1')
	pix = image.load()
	X = image.size[0]
	Y = image.size[1]
	return [[pix[x,y] for x in range(X)] for y in range(Y)]

def show(i):
	"""
	Show an image from image matrix.

	:param i: image matrix
	:type i: list
	"""
	print get_w(i)
	image = Image.new(format(i),(get_w(i),get_h(i)))
	image.putdata([pixel for F in matrix(i) for pixel in F])
	image.show()

def save(img, nomf):
	"""
	Save an image from image matrix. 

	:param img: image matrix
	:type img: list
	:param nomf: filename
	:type nomf: str
	"""
	image = Image.new(format(img),(get_w(img),get_h(img)))
	image.putdata([pixel for F in matrix(img) for pixel in F])
	image.save(nomf)
