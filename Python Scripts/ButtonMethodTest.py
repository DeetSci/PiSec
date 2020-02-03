def sendMessage():
    msg = "The front door has been opened."
    server.sendmail("petermorley4@gmail.com", "petemorley3@gmail.com", msg)


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("petemorley4@gmail.com", "WorkEmail1")

sendMessage()
