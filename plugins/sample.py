import random

def process(route, content):

	if len(route) > 1:
		if route[1]=="counter":
			return counter(route, content)
		elif route[1]=="random2":
			return random(route, content)

	s = "<h1>Hello!</h1>"
	s += "<p>This is an example of a plugin</p>"
	s += "<p>Try also: <a href=/sample/counter>counter</a> and <a href=/sample/random>random</a></p>"
	return s

def counter(route, content):
	if "value" in content:
		s = ""
		for x in range(0, int(content["value"])+1):
			s += str(x)+"<br>"
		return s

	else:
		return "Please pass a counter parameter, <a href=/sample/counter?value=100>like this</a>"

def random2(route, content):
	return str(random.random())
