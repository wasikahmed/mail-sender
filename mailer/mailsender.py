from email.message import EmailMessage
import ssl
import smtplib
from django.conf import settings


class MailSender:
    def __init__(self):
        self.email_sender = settings.EMAIL_HOST_USER
        self.email_password = settings.EMAIL_HOST_PASSWORD
        self.email_receiver = []
        self.email = EmailMessage()

    def add_email_receiver(self, email_receiver: str):
        self.email_receiver.append(email_receiver)

    def create_email(self, subject: str, body: str):
        self.email = EmailMessage()
        self.email['From'] = self.email_sender
        self.email['To'] = ", ".join(self.email_receiver)
        self.email['Subject'] = subject
        self.email.set_content(body)

    def send_email(self):
        if not self.email_receiver:
            raise ValueError("At least one recipient is required")

        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT, context=context) as smtp:
                smtp.login(self.email_sender, self.email_password)
                smtp.sendmail(self.email_sender, self.email_receiver, self.email.as_string())
            return {"message": f"Email sent successfully to {len(self.email_receiver)} recipients"}
        except Exception as e:
            return {"error": str(e)}
