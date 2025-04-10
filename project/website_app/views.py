from django.shortcuts import render
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
import os
from django.conf import settings
from email.message import EmailMessage
import ssl
import smtplib

@method_decorator(csrf_exempt, name='dispatch')
class FormSendMail(APIView):
    def post(self, request, *args, **kwargs):
        dict_data = request.data

        email_body = f"""
        Name: {dict_data.get("name")}
        Email: {dict_data.get("email")}
        Phone No: {dict_data.get("number")}
        Subject: {dict_data.get("service")}
        Message:
        {dict_data.get("message")}
        """
        print('emailbody: ', email_body)
       
        sender_email = os.getenv("SENDER_EMAIL", settings.EMAIL_ID)
        sender_password = os.getenv("SENDER_PASSWORD", settings.EMAIL_PASSWORD)
        recipient_email = "akanksha@grandortus.com"  # Replace with your recipient address

        try:
            # Create the email message
            email_msg = EmailMessage()
            email_msg['Subject'] = dict_data.get("service")
            email_msg['From'] = sender_email
            email_msg['To'] = recipient_email
            email_msg.set_content(email_body)

            # Email sending
            if ssl._create_unverified_context():
                context = ssl._create_unverified_context()
                with smtplib.SMTP("mail.grandortus.com", 587) as server:
                    server.starttls(context=context)
                    server.login(sender_email, sender_password)
                    server.send_message(email_msg)
                    
            else:
                context = context = ssl.create_default_context(cafile="/opt/homebrew/etc/openssl@3/cert.pem")
                with smtplib.SMTP("mail.grandortus.com", 587) as server:
                    server.starttls(context=context)
                    server.login(sender_email, sender_password)
                    server.send_message(email_msg)

            return Response({"success": True})
        except Exception as e:
            return Response({"success": False})



