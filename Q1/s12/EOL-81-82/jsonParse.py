def getTextSince(txt, chars):
	print txt
	n_of_subdics = 0
	position = 0
	start_pos = 0
	for char in txt:
		if char == chars[0]:
			if n_of_subdics == 0:
				start_pos = position
			n_of_subdics += 1
		if char == chars[1]:
			if n_of_subdics == 1:
				return txt[start_pos+1:position]
			else:
				n_of_subdics -= 1
		position += 1
	return ""

def parseJSON(txt, end=""):
	position = 0
	for char in txt:
		if char == "{":
			dic = {}
			properties = getTextSince(txt[position:], ("{", "}")).split(",")
			print properties
			for prop in properties:
				prop = prop.split(":")
				print prop
				dic[prop[0]] = parseJSON(prop[1])
			return dic
		if char == "'" or char == "\"":
			return txt[1:-1]

print parseJSON("{'jordi': 'hola'}")