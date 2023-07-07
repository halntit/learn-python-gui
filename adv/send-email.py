import smtplib

sender = "halntit@gmail.com"
receiver = "halntit@gmail.com"
password = "123Lenguyen!23"
subject = "I use python"
body = "Can you see it?"

message = f"""From: Python User{sender}
To: Codeer{receiver}
Subject: {subject}\n\n{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    server.sendmail(sender, receiver, message)
    server.quit()
except smtplib.SMTPAuthenticationError as e:
    print("Something went wrong")
    print(e.args)
