def nDeXifres(n):
	n = str(n)
	i = 0
	s = 0
	while i < len(n):
		s += int(n[i])
		i+=1
	return s

i = 5
# Suma les xifres de tots els números des de 5 fins a 102
while i <= 102:
    print "Suma les xifres de", i, ":", nDeXifres(i)
    i+=1
