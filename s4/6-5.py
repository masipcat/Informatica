n = input("Introdueix un nombre:")

k = 1
r = 1
while k <= n:
    r *= k
    k+=1

print "El factorial de", n, "es:", r
