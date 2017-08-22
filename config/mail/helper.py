import getpass, base64  # well isn't this a recipe for disaster, see readme

server = raw_input("Remote server? ") or "imap.gmail.com"
email = raw_input("Email address? ")
other = getpass.getpass()

vals = base64.b64encode("\n".join((server, email, other)))
f = open("contents", "w")
f.write(vals)
f.close()
