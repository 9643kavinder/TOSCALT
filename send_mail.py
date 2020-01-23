import os
import smtplib
server = smtplib.SMTP("smtp.gmail.com",587)
server.ehlo()
server.starttls()
server.login("MAIL_ID","PASSWORD")
server.sendmail("SENDER_MAIL_ID","RECEIVER_MAIL_ID","CONTENT")
server.close()
print("mail has been sent")
