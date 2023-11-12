import smtplib, ssl, os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "akash.burner.2003@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "akash.burner.2003@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)