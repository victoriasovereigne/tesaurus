import re
import string
import json

def raw():
	f = open('tesaurus.txt', 'r')
	w = open('hasil0.txt', 'w')
	lines = f.readlines()

	newlines = []

	for line in lines:
		l = re.sub('\t', ' ', line)
		l = l.rstrip()
		l = re.sub(r'(?<=\w)\s{2,}(?=\w)', '', l)

		# buang FF dan CAN
		if re.match('^[\w\n\s,;()-]+$', l) is not None:
			newlines.append(l)

	for line in newlines:
		if line.endswith(','):
			w.write(line+' ')
		elif line.endswith('-'):
			w.write(line[:-1])
		else:
			w.write(line+'\n')

	f.close()
	w.close()

tags = ['a','adv','n','num','p','pron','v', 'ki']

def toDict():
	f = open('hasil0.txt', 'r')	

	lines = f.readlines()
	mydict = {}
	key = ''
	tag = ''
	words = []

	for line in lines:

		words = line.split(' ')
		words = [x.rstrip(',;\n') for x in words if x != '']		
		# print words

		if words[0] != 'ant' and len(words) > 1:
			if words[1] in tags:
				key = words[0]
				tag = words[1]
				mydict[key] = {"tag":words[1], "sinonim":words[2:]}
			elif len(words) > 2 and words[2] in tags:
				key = words[0]
				tag = words[2]
				mydict[key] = {"tag":words[1], "sinonim":words[3:]}

		elif words[0] == 'ant':
			mydict[key]['antonim'] = words[1:]

	f.close()

	for key in mydict.keys():
		print key + " --> " + str(mydict[key])

	return mydict

def writeToJson(data, filename):
	with open(filename +'.json', 'a') as outfile:
		json.dump(data, outfile, ensure_ascii=False)

	return outfile

# raw()
dicta = toDict()
writeToJson(dicta, 'dict')