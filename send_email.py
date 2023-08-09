import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    email = "eunicepatrina0@gmail.com"
    password = "vnsmyhpurcjzbzld"

    receiver = "eunicepatrina2000@gmail.com"

    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(email, password)
        server.sendmail(email, receiver, message)
