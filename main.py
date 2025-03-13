import os
from email.message import EmailMessage
import ssl
import  smtplib


email_sender = "aponwasikahmed@gmail.com"
email_password = os.environ.get('MAIL_SENDER_PASS')
email_receiver = "apon.wasik2001@gmail.com"

subject = "Test Email"
body = "This is a test email"

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
