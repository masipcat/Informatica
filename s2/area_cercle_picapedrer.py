#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def area_picapedrer(r):
    return (r*2)**2 * 0.8

def area_picapedrer2(r):
    print "L'àrea és:", area_picapedrer(r)

radi = input("Introdueix un radi: ")

print "L'àrea de la circunferència aprox. de radi", radi, "és:", area_picapedrer(radi), "u2"
