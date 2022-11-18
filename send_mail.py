import smtplib
from email.mime.text import MIMEText


def send_mail(customer, seller, rate, comment):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'a4da582c419fd1'
    password = '2e1eb243422276'
    message = f'<h3>New Rating Submitted!!!</h3><ul><li>CUSTOMER NAME: {customer}</li><li>SELLER NAME: {seller}</li><li>RATING: {rate}</li><li>REVIEW: {comment}</li></ul>'
    sender_mail = 'tiwarivarun962@gmail.com'
    reciever_mail = 'varun131109@gmail.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Rating Manager'
    msg['From'] = sender_mail
    msg['To'] = reciever_mail
    
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_mail, reciever_mail, msg.as_string(()))