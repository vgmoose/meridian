import os

class Responder(BaseResponder):
	
	def init(self):
		self.curdir = os.path.expanduser("~")
	
	def process(base, args):
		cmd = base[1]		
		return cmd

