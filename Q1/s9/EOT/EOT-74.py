import sys

valors = sys.argv[1:]
length = len(valors)

if length > 0:
	valors.sort()
	if length % 2 == 0:
		mediana = (float(valors[length/2 - 1]) + float(valors[length/2])) / 2
	else:
		mediana = valors[length / 2]
	print mediana
else:
	print "No hi ha valors"
