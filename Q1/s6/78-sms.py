def toSMS(s):
	s = s.lower()
	s = s.replace("que", "k")
	s = s.replace("tal", "tl")
	s = s.replace("ss", "s")
	s = s.replace("fas", "ase")
	s = s.replace("de", "d")
	s = s.replace("hola", "ola")
	return s

print "Hola que fas? Estic passant de tot!!"
print toSMS("Hola que fas? Estic passant de tot!!")
