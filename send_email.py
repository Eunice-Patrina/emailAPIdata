import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    email = "username@gmail.com"
    password = "password"

    receiver = "username@gmail.com"

    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(email, password)
        server.sendmail(email, receiver, message)
