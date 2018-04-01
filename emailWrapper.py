import smtplib

from  email.MIMEMultipart import MIMEMultipart
from  email.MIMEText import MIMEText

import config.config as cfg

_login_ = cfg.email['email']
_password_ = cfg.email['key']

def sendEmail(to, result, datetime):
    server = setupEmail()
    email = createMessenge(to, result, datetime)
    server.sendmail(_login_, to, email)
    server.quit()

def sendEmailDS(to, result, datetime, itsRaining):
    server = setupEmail()
    email = createMessengeDS(to, result, datetime, itsRaining)
    server.sendmail(_login_, to, email)
    server.quit()

def setupEmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(_login_, _password_)
    return server

def createMessenge(to, result, datetime):
    body = "Stats time: " + str(datetime) + " || temperature: " + str(result.temperature) + "C || humidity: " + str(result.humidity) + "%"

    msg = MIMEMultipart()
    msg['From'] = _login_
    msg['To'] = to
    msg['Subject'] = 'House report'
    
    msg.attach(MIMEText(body, 'plain'))
    email = msg.as_string()
    return email

def createMessengeDS(to, result, datetime, itsRaining):
    print(itsRaining)
    rain = ""
    if itsRaining == 0:
        rain = "not"
    body = "Stats time: " + str(datetime) + " || temperature inside: " + str(result[0]) + " celsius  || temperature outside: " + str(result[1]) + " celsius. Currently " + rain + " raining!"

    msg = MIMEMultipart()
    msg['From'] = _login_
    msg['To'] = to
    msg['Subject'] = 'House report'
    
    msg.attach(MIMEText(body, 'plain'))
    email = msg.as_string()
    return email

