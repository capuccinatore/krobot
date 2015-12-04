#http://stackoverflow.com/questions/882712/sending-html-email-using-python
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class MailAgent(object):
	"""docstring for MailAgent"""
	def __init__(self, mail, smtp, pseudo, passw):
		super(MailAgent, self).__init__()
		self.mail = mail
		self.smtp = smtp
		self.pseudo = pseudo
		self.passw = passw

	def send(self, dest, object, text):
		
		# Create message container - the correct MIME type is multipart/alternative.
		msg = MIMEMultipart('alternative')
		msg['Subject'] = "Link"
		msg['From'] = self.mail
		msg['To'] = dest

		# Create the body of the message (a plain-text and an HTML version).
		html = "<html><head></head><body>{0}</body></html>".format(text)

		# Record the MIME types of both parts - text/plain and text/html.
		part1 = MIMEText(text, 'plain')
		part2 = MIMEText(html, 'html')

		# Attach parts into message container.
		# According to RFC 2046, the last part of a multipart message, in this case
		# the HTML message, is best and preferred.
		msg.attach(part1)
		msg.attach(part2)
		# Send the message via local SMTP server.
		mail = smtplib.SMTP(self.smtp, 587)

		mail.ehlo()
		mail.starttls()

		mail.login(self.pseudo, self.passw)
		mail.sendmail(self.mail, dest, msg.as_string())
		mail.quit()