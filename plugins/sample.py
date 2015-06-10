import random, baseresponder

class Responder(baseresponder.BaseResponder):
	def process(self, args, data):
		super(Responder, self).process(args, data)
		if len(args) > 1:
			if args[1]=="counter":
				return self.counter(args, data)
			elif args[1]=="random":
				return self.random2(args, data)

		s = "<h1>Hello!</h1>"
		s += "<p>This is an example of a plugin</p>"
		s += "<p>Try also: <a href=/sample/counter>counter</a> and <a href=/sample/random>random</a></p>"
		return s

	def counter(self, route, content):
		if "value" in content:
			trials = int(content["value"])+1
			if trials > 101:
				return (413, "Error! Enter a number smaller than 100")
			s = ""
			for x in range(0, trials):
				s += str(x)+"<br>"
			return s

		else:
			return "Please pass a counter parameter, <a href=/sample/counter?value=100>like this</a>"

	def random2(self, route, content):
		return str(random.random())
