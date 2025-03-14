from email.message import EmailMessage
import ssl
import smtplib


class MailSender:
    def __init__(self, email_sender: str, email_password: str):
        self.email_sender = email_sender
        self.email_password = email_password
        self.email_receiver = []
        self.email = EmailMessage()

    def add_email_receiver(self, email_receiver: str):
        self.email_receiver.append(email_receiver)

    def add_receivers_from_file(self, file_path: str):
        try:
            with open(file_path, "r") as file:
                for line in file:
                    email = line.strip()
                    if email:
                        self.add_email_receiver(email)
            print(f"Loaded {len(self.email_receiver)} recipients from {file_path}")
        except FileNotFoundError:
            print(f"Error: File {file_path} not found")

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
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(self.email_sender, self.email_password)
                smtp.sendmail(self.email_sender, self.email_receiver, self.email.as_string())
            print(f"Email sent successfully to {len(self.email_receiver)} recipients")
            print("List of recipients:")
            for recipient in self.email_receiver:
                print(recipient)
        except Exception as e:
            print("Failed to send email:", e)
