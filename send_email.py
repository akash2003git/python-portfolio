import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "akash.burner.2003@gmail.com"
password = "nfzk wzuk xnzd kxbo"

receiver = "akash.p.tayade@gmail.com"
message = """\
Subject: Hi! 
HELLO WORLD
"""

my_context = ssl.create_default_context()

with smtplib.SMTP_SSL(host, port, context=my_context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
