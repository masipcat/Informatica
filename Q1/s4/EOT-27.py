prompt = "Introdueix un nombre: "
n = input(prompt)
r = 0
while n != 0:
    r += n
    n = input(prompt)

print "\nLa suma dels nombres es:", r
