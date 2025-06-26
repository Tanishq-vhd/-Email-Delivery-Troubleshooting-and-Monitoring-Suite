import smtplib, ssl
from email.mime.text import MIMEText

def send_email_smtp(sender_email, receiver_email, smtp_server, port, password, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print(" Email sent via SMTP.")
    except Exception as e:
        print(" SMTP Error:", e)
