### Plugin: email
This plugin is intended to fetch unread emails from a remote IMAP server and mark them read

#### Routes

| route             | action |
| -----             | ------ |
| /mail            | fetch any unread email, return it, and mark it as read |
| /mail/logout     | disconnect from the remote server |


#### Intended Use
The intended use is to just poll /mail to get new email every so often, and hopefully have it automatically
mark it as read as it fetches and returns it. It will automatically try to reconnect if the connection
to the IMAP server is down.

#### Credentials Storage
At this time, meridian does not integrate or support any type of keychain management. Run the python
helper script in this folder to generate an cleartext file containing the required parameters.

This file should be protected on disk such that nobody besides meridian can read it.
