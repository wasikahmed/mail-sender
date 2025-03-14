import os

from sender import MailSender


def main():
    email_sender = "aponwasikahmed@gmail.com"
    email_password = os.environ.get("MAIL_SENDER_PASS")

    mailer = MailSender(email_sender, email_password)
    mailer.add_receivers_from_file("recipients.txt")

    subject = "Welcome to Mail Sender"
    body = "This is a test email sent to multiple recipients."
    mailer.create_email(subject, body)
    mailer.send_email()


if __name__ == "__main__":
    main()
