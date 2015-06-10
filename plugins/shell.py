import os, baseresponder, subprocess

class Responder(baseresponder.BaseResponder):
	
	def __init__(self):
		super(Responder, self).__init__()
		self.curdir = os.path.expanduser("~")
	
	def process(self, args, data):
		super(Responder, self).process(args, data)
		
		# default cmd if none is specified
		cmd = "true"

		# if a command is specified
		if "cmd" in data:
			cmd = data["cmd"]	
			
		# for debug mode just print the command, don't run it
		if "debug" in data:
			return cmd
		
		try:
			# run the command
			output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
		except subprocess.CalledProcessError as e:
			return str(e.returncode) +": "+e.output
		
		# return the output from the command
		return output

