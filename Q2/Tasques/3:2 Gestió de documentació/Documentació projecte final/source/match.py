#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
============
match module
============

Use this module to compare if two images are similar.
"""

# DEV: Jordi Masip

#import imgio, tranf, split, sys, os
#from utiles import *
#from img import *

def compare_image(img, pttrn):
	"""
	Return a floating value between 0-1. 

	:param img: main image
	:type img: list
	:param pttrn: pattern
	:type img: list
	"""
	total_pixels, coincidence = len(img[0]) * len(img), 0
	
	for i in range(len(img)):
		for j in range(len(img[i])):
			if img[i][j] == pttrn[i][j]:
				coincidence += 1
	if total_pixels != 0:
		return coincidence / float(total_pixels)
	return 0

def load_patterns(prefix):
	"""
	Return a list of tuples that first element of each tuple is the value that represents the pattern. The second element is a image matrix

	:param prefix: filename prefix
	:type prefix: str
	"""
	debug("Recordar canviar a load_patterns() -> range(10)")
	return [(num, imgio.read_bn(str(prefix) + str(num) + ".jpeg")) for num in range(10)]

def match(img, patlst):
	"""
	Return an integer between 0-9 that represents the number in the image. If no number in the image, return -1.

	:param img: main image
	:type img: list
	:param patlst: list of patterns
	:type img: list
	"""
	# Mida de la imatge
	img_size = (len(img[0]), len(img))

	# ((int) valor de la imatge, (float) coincidence)
	best_match = (-1, 0.0)

	for i, pattern in enumerate(patlst):
		pattern = ("1", pattern[1])

		debug("img_size " + str(img_size))
		pattern_size = (get_w(pattern), get_h(pattern))
		debug("pattern_size " + str(pattern_size))
		
		if img_size[1] >= pattern_size[1]:
			img = tranf.scale(("1", img), pattern_size[1])[1]
			img_size = (get_w(("", img)), get_h(("", img)))
			
		else:
			pattern = tranf.scale(pattern, img_size[1])[1]
			pattern_size = (get_w(("1", pattern)), get_h(("1", pattern)))

		if img_size[0] >= pattern_size[0]:
			scroll = img_size[0] - pattern_size[0]
			
			big_size = img_size[0]
			small_size = pattern_size[0]
			
			big_image = img
			if isinstance(pattern, tuple):
				small_image = pattern[1]
			else:
				small_image = pattern	
		else:
			scroll = pattern_size[0] - img_size[0]

			big_size = pattern_size[0]
			small_size = img_size[0]
			if isinstance(pattern, tuple):
				big_image = pattern[1]
			else:
				big_image = pattern
			small_image = img

		debug("Scroll: " + str(scroll))
		
		# Es desa la nova mida
		debug("pattern_size_scalated " + str(pattern_size))
		last_coincidence = -1
		
		for position in range(scroll+1):
			croped_img = split.image_slice_vertical(big_image, position, small_size + position)
			coincidence = compare_image(croped_img, small_image)
			if coincidence > last_coincidence:
				last_coincidence = coincidence
		
		if best_match[1] < last_coincidence:
			best_match = (i, last_coincidence)

	debug("El best_match es " + str(best_match))
	return best_match[0] if best_match[1] >= 0.6 else -1
