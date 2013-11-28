#!/usr/bin/env python
# -*- coding: utf-8 -*-

def f(a):
    a = a + 5
    return a

b = 0
f(b)
print b, "," ,
b = f(b)
print b

'''
defineix b = 0, crida a f(0) i retorna 0+5 (però no es recull el resulat). Després mostra en pantalla "b," (sense salt de línia) i després torna a cridar f(0) i mostra el valor al costat de la cadena anterior.
'''
