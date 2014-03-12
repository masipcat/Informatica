i = 0
primer = 0
proper = 0
while i < 5:
    n = input("Introdueix un nombre: ")
    if i == 0:
        primer = n
        proper = primer
    if primer == proper or n <= proper and n >= primer:
        proper = n
    i+=1

print "\nEl numero mes proper a", primer,"es el", proper
