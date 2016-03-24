import re
import string
import json

def raw():
	f = open('tesaurus.txt', 'r')
	w = open('hasil0.txt', 'w')
	lines = f.readlines()

	newlines = []

	for line in lines:
		l = re.sub('\t', ' ', line) # replace tab dengan dua spasi
		l = l.rstrip() # buang spasi diakhir huruf
		l = re.sub(r'(?<=(ant))\s{2,}(?=\w)', ' ', l) # buang spasi antara dua huruf
		l = re.sub(r'(?<=\w)\s{2,}(?=\w)', '', l) # buang spasi antara dua huruf
		l = re.sub(r'\d+','', l) # buang digit
		l = l.replace('(cak)', '').replace('(ki)', '')
		l = l.replace('\x0C', '')

		# buang FF dan CAN
		if re.match('^[\w\n\s,;()-]+$', l) is not None:
			if len(newlines) == 0:
				newlines.append(l)
			elif len(newlines) > 0:
				if l.startswith(','):
					newlines[len(newlines)-1] = newlines[len(newlines)-1] + l
					print l	
				elif l.startswith('('):
					newlines[len(newlines)-1] = newlines[len(newlines)-1] + ' ' + l
					print l	
				else:					
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
	f = open('tesaurus-proses.txt', 'r')	

	lines = f.readlines()
	mydict = {}
	key = ''
	tag = ''
	sinonim = []
	antonim = []
	words = []

	for line in lines:
		t = re.compile(' (a|adv|n|num|p|pron|v) ')
		match = t.search(line)

		# cek apakah diawali dengan --
		if '--' in line:
			line = line.replace('--', key).lstrip().rstrip()
			words = line.split(' ')
			awal = ' '.join(words[:2])			
			
			if match is None:
				mytag = tag
				end = len(awal)
			else:
				start = match.start()
				end = match.end()
				mytag = line[start:end].lstrip().rstrip()
			
			mydict[awal] = {}
			mydict[awal]['tag'] = mytag
			mysinonim = line[end:].replace(';',',').lstrip().rstrip().split(',')
			mysinonim = [x.lstrip().rstrip(',;\n') for x in mysinonim if x != '']	
			mydict[awal]['sinonim'] = mysinonim
		else:
			# cek apakah ada tag di line
			if match is not None:
				start = match.start()
				end = match.end()
				key = line[0:start].lstrip().rstrip()
				tag = line[start:end].lstrip().rstrip()
				sinonim = line[end:].replace(';',',').lstrip().rstrip().split(',')
				sinonim = [x.lstrip().rstrip(',;\n') for x in sinonim if x != '']	

				if ',' in key:
					key = key.split(',')[0]

				if key in mydict.keys():
					if 'sinonim' in mydict[key].keys():					
						mydict[key]['sinonim'].extend(sinonim)
				else:
					if len(key) > 0:
						mydict[key] = {}
						mydict[key]['tag'] = tag
						mydict[key]['sinonim'] = sinonim
				# else:
				# 	print line
				# print key + ' | tag: ' + tag + ' | sinonim: ' + str(sinonim)
			else:
				if ' ant ' in line and len(key) > 0:
					words = line.lstrip().rstrip().split(' ')
					antonim = words[1:]
					antonim = [x.lstrip().rstrip(',;\n') for x in antonim if x != '']	
					mydict[key]['antonim'] = antonim
					# print 'antonim: ' + str(antonim)		
		
		antonim = []

	f.close()

	for key in sorted(mydict.keys()):
		print key + " --> " + str(mydict[key])

	return mydict

def writeToJson(data, filename):
	with open(filename, 'w') as outfile:
		json.dump(data, outfile, ensure_ascii=False, indent=4)

	return outfile

def readFromJson(filename):	
	with open(filename) as data_file:
		data = json.load(data_file)	

	return data

def getSinonim(word):
	myjson = readFromJson('dict.json')
	return myjson[word]['sinonim']

# raw()
dicta = toDict()
writeToJson(dicta, 'dict.json')

# print getSinonim('acuh')