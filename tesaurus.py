# ==================================================
# Written in March 2016 by Victoria Anugrah Lestari
# ==================================================
import json

# ==================================================
# Membaca dictionary dari json
# ==================================================
def load(filename):	
	with open(filename) as data_file:
		data = json.load(data_file)	

	return data

# load dictionary
mydict = load('dict.json')

# ==================================================
# Mencari sinonim suatu kata
# ==================================================
def getSinonim(word):
	if word in mydict.keys():
		return mydict[word]['sinonim']
	else:
		return []

# ==================================================
# Mencari antonim suatu kata
# ==================================================
def getAntonim(word):
	if word in mydict.keys():
		if 'antonim' in mydict[word].keys():
			return mydict[word]['antonim']

	return []

print getSinonim('senang')
print getSinonim(getAntonim('senang')[0])
print getSinonim('anna')