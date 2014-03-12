n = str(raw_input("Introdueix un numero: "))
i = 0
s = 0
while i < len(n):
	s += int(n[i])
	if s > 9 and i == len(n) - 1:
		n = str(s)
		i = 0
		s = 0
	else:
		i+=1

print s