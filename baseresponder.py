import threading

class BaseResponder:
	# all plugins will extend this BaseResponder, but implementing
	# any of the methods are optional depending on what the plugin
	# needs to accomplish

	def init(self):
		# code to be run when the plugin is first imported

		# returns true if initialization is successful,
		# false if unsuccessful.

		# a dict containing all of the currently running
		# asychronous tasks (id -> task object)
		self.tasks = []

	def process(self, args, data):
		# this code is called upon the visiting of the
		# resource: http://domain.com/pluginname

		# args will contain the URL from the root, with 
		# args[0] containing the plugin name (much like 
		# sys.args[0] would contain the program name)
		# eg. /pluginname/arg1/arg2/arg3/arg4/arg5
		
		# data will contain a dict of keys and values
		# that has been passed through either get or post
		# eg. /pluginname?key1=value1&key2=value2

		# this method will return a string of what the response
		# is, or an int representing the response code.

		# by default return not found (hides plugin)	
		return 404

	def create_task(self, task):
		# a plugin can call create_task to begin an asyncronous
		# operation.

		# create a thread for this task
		thr = threading.Thread(target=task.main, args=task.args, kwargs={})

		# add it to the local task dict
		self.tasks[task.id] = thr

		# begin the task in the background
		thr.start()

	def wait_task(self, id):
		# this method will wait until the designated task id
		# is completed
		
		if id in self.tasks:
			# wait for it
			self.tasks[id].join()
			return True
		# if the task isn't running return false
		else:
			return False

	def stop_task(self, id):
		# this method will instantly halt the task with the given
		# id

		# if the task with the given id is in the task dict
		if id in self.tasks:

			# interrupt it if it is running
			if self.tasks[id].is_alive():
				self.tasks[id].interrupt()
				return False

			# otherwise, just delete the dead task
			del self.tasks[id]

		return True
			
		


