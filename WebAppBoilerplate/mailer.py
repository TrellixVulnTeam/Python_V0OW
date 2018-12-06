from flask import Flask
from flask_mail import Mail
from flask_mail import Message
import smtplib

app = Flask(__name__)

server = smtplib.SMTP('smtp.gmail.com', 587)

    #Next, log in to the server
# server.starttls()
server.login("senderId", "pwd")
msg = Message('Shashank - Python Mail',['shash.dhyani@gmail.com'])
reps = server.sendmail("workaholics.onlinejobportal@gmail.com","shash.dhyani@gmail.com",'Hey! Did you recieve the bite of python yet??')
# server.quit()
print('done')
