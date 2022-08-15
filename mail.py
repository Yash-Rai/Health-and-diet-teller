import smtplib

def sendmail(receiver,message) :
    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login("pythonproject2007@gmail.com","rishiben18")
    server.sendmail("pythonproject2007@gmail.com",receiver,message)
    server.quit()
