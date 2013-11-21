import sys

valors = sys.argv[1:]
length = len(valors)

if length > 0:
	sumatori = 0.
	for i in valors:
		sumatori += float(i)
	print sumatori / length
else:
	print "No hi ha valors"
