import os, baseresponder, re, random

class Responder(baseresponder.BaseResponder):
	
	def __init__(self):
		super(Responder, self).__init__()
		
		# open the word list
		words = open("config/japanese/wordlist.txt", "r")
		
		# parse them into the data array
		self.data = []
		lastcat = ""
		
		for line in words:
			
			# if it's a category, set the current category
			if line.startswith("Category: "):
				pass
#				lastcat = line[10:-1].lower()
#				self.data[lastcat] = []
				
			# otherwise, add this entry to the current category
			else:
				halves = line.split(' \xe2\x80\x93 ')
				word = halves[0]
				answer = ' '.join(re.findall(r'(.*?)\(.*?\)', halves[1]))
				notes = ' '.join(re.findall(r'\((.*?)\)', halves[1]))
				self.data.append((word, notes, answer))
				
#		print self.data
	
	def process(self, args, data):
		super(Responder, self).process(args, data)
				
		# find the target word index either from arguments or randomly
		if len(args) > 1:
			tindex = int(args[1])
			if len(args) <= 2:
				return " ".join(self.data[tindex])
		else:
			tindex = int(random.random()*len(self.data))
			
		# if they are requesting a specific part (word, answer, notes) return it
		if len(args) > 2:
			offset = int(args[2])
		else:
			return str(tindex)
		
		# echo back the category and entry index
		return self.data[tindex][offset]

