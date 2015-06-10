import baseresponder

class Responder(baseresponder.BaseResponder):
	def process(self, args, data):
		super(Responder, self).process(args, data)
		return "This is the root module"
