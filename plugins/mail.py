import random, baseresponder

import sys
import imaplib
import getpass
import email
import email.header
import datetime
import base64

class Responder(baseresponder.BaseResponder):

	def __init__(self):
		super(Responder, self).__init__()

		# only setup properties
		content = base64.b64decode(open("config/mail/contents", "r").read()).split("\n")
		self.IMAP_SERVER = content[0]
		self.EMAIL_ACCOUNT = content[1]
		self.OTHER_VALUE = content[2]

	def process(self, args, data):
		"""
		Simply return any unread emails at the connected IMAP inbox.
		If the connection to the IMAP server is dead, a reconnect will be attempted first
		"""
		super(Responder, self).process(args, data)

		try:	
			# try to fetch new mail
			s = self.fetch_mail()
		except:
			# try a re-login
			self.attempt_login()

			try:
				# and fetch again
				s = self.fetch_mail()
			except Exception, e:
				# report an error
				s = "Issue fetching mail, please check configuration and connections: " + e.message

		# return the content
		return s

	def attempt_login(self):
		"""
		Attempt a login using the credentials that are configured
		This can throw an error if it fails
		"""
		self.M = imaplib.IMAP4_SSL(self.IMAP_SERVER)

		# do the actual login call
		rv, data = self.M.login(self.EMAIL_ACCOUNT, self.OTHER_VALUE)

	def fetch_mail(self):
		"""
		While connected, fetch and return any unread mail from the remote server
		This method will also mark the mail as read
		"""
		s = ""
		self.M.select("Inbox")

		rv, data1 = self.M.search(None, "UnSeen") 
		if rv != "OK":
			return "An issue was encountered retreiving unread email"

		for x in data1[0].split():
			# get the x-th unread message that was returned from the server
			rv, data = self.M.fetch(x, "(RFC822)")

			# get subject and sender 
			message = email.message_from_string(data[0][1])
			sender = message["from"]
			subject = message["subject"]

			# get the body
			body = ""
			if message.get_content_maintype() == "multipart":
				for part in message.walk():
					if part.get_content_type() == "text/plain":
						body = part.get_payload(decode=True)
					else:
						continue

			# append this to all things that will be returned
			s += "%s: %s\n%s\n\n" % (sender, subject, body)

			# mark as read
			self.M.store(x,'+FLAGS','\Seen')

		return s

	def logout(self):
		"""
		Disconnect from the remote server
		"""
		self.M.logout()
