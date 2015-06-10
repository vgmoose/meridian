import baseresponder

class Responder(baseresponder.BaseResponder):
	def process(self, args, data):
		super(Responder, self).__init__()
		return 200
