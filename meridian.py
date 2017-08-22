#~ /bin/python

# built in libraries
import os, sys, imp

# local library
import baseresponder

sys.dont_write_bytecode = True

# import necessary external libraries
try:
	import cherrypy
except:
	print "missing requirement! run pip install -r requirements.txt"
	exit()

# add plugins to build path
sys.path.insert(0, 'plugins')

plugins = {}

# load registered plugins
plugin_dir = os.listdir("plugins")
for filename in plugin_dir:
	if filename.endswith(".py"):
		name = filename.replace(".py", "")
		plugins[name] = __import__(name)
        
responders = {}

# load responders from plugins and call init functions
for name in plugins:
	module = plugins[name]
	if hasattr(module, "Responder"):
		try:
			responders[name] = module.Responder()
		except Exception, e:
			print("Issue loading "+name+" plugin! " + e.message)

class RESTServer(object):
	@cherrypy.expose
	def default(self,*args,**kwargs):

		if len(args) > 0:
			route = args[0]
		else:
			route = "root"

		# delegate its arguments to the appropriate plugin
		if route in plugins:
			output = responders[route].process(args, kwargs)
			if isinstance(output, tuple):
				cherrypy.response.status = output[0]
				return output[1]
			elif isinstance(output, int):
				cherrypy.response.status = output
				return ""
			else:
				return output
		else:
			cherrypy.response.status = 404
			return "Undefined!<br/>No responder for: "+route+"<br/>You gave me:"+str(kwargs)
					

cherrypy.quickstart(RESTServer())
