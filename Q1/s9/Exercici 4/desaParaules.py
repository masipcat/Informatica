#!/usr/bin/env python
# -*- coding: utf-8 -*

import sys

if len(sys.argv) > 1:
	f = open("paraules.txt", "w")
	content = ""
	for paraula in sys.argv[1:]:
		content += "\n" + paraula
	f.write(content[1:])
	f.close()
	print "S'ha desat correctament a 'paraules.txt'"
else:
	print "No s'han trobat paraules"
