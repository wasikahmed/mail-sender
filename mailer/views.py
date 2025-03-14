from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .mailsender import MailSender


class SendEmailView(APIView):
    def post(self, request):
        data = request.data
        recipients = data.get("recipients", [])
        subject = data.get("subject", "")
        body = data.get("body", "")

        if not recipients or not subject or not body:
            return Response({"error": "recipients, subject, and body are required"}, status=400)

        mail_sender = MailSender()
        for email in recipients:
            mail_sender.add_email_receiver(email)

        mail_sender.create_email(subject, body)
        response = mail_sender.send_email()

        if "error" in response:
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(response, status=status.HTTP_200_OK)
