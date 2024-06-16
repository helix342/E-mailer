from email.message import EmailMessage
import ssl
import smtplib

enter = input("Enter mail you want to send to : ")
sender = "SENDER_MAIL_ID"
receiver = enter
password = "SENDER_MAIL_AUTH_PASSWORD"
subject = "You've Got Mail"
body = "Monty Python is not the best circus."

em = EmailMessage()
em["From"] = sender
em['To'] = receiver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
    try:
        smtp.login(sender, password)
        print("Logged in...")
        smtp.sendmail(sender, receiver, em.as_string())
        print("Mail(s) has been sent")
    except smtplib.SMTPAuthenticationError:
        print("unable to sign in")
