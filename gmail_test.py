
import smtplib

def alart_email():
	sender = "cjeter@gmail.com"
	receiver = "cjeter@gmail.com"
	message = """From: SAFE DOOR <safe@outcast.homeunix.org>
	To: <cjeter@gmail.com>
	Subject: SMTP e-mail test
	This is a test e-mail message.
	"""

	try:
		session = smtplib.SMTP('smtp.gmail.com',587)
		session.ehlo()
		session.starttls()
		session.ehlo()
		session.login(sender,'vygqvutorvirnpsa')
		session.sendmail(sender,receiver,message)
		session.quit()
	except smtplib.SMTPException:
		print('Error')
	return;
alart_email()
