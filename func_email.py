def alart_email():
    sender = "cjeter@gmail.com"
    recipient = "cjeter@gmail.com"
    cc = "7856919005@txt.att.net"
    email_subject = "SAFE ALART - DOOR OPEN"
    email_body = "I've detected that the door of the safe is OPEN!"
    headers = "\r\n".join([
            "from: " + sender,
            "subject: " + email_subject,
            "to: " + recipient,
            "cc: " + cc,
            "mime-version: 1.0",
            "content-type: text/html"])
    toaddrs = [recipient, cc]
    content = headers + "\r\n\r\n" + email_body
        try:
            session = smtplib.SMTP('smtp.gmail.com',587)
            session.set_debuglevel(0)
            session.ehlo()
            session.starttls()
            session.ehlo()
            session.login(sender,'vygqvutorvirnpsa')
            session.sendmail(sender,toaddrs,content)
            session.quit()
        except smtplib.SMTPException:
            print('Error')
        return;

