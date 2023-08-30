import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP_SSL('Smtp.gmail.com', 465)

server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()

server.login('afroproplayer@gmail.com', password)
msg = MIMEMultipart()
msg['From'] = 'codigoDoManu'
msg['To'] = 'zolaconnie@gmail.com'
msg['Subject'] = 'Just a test'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'Screenshot 2023-08-09 at 14.34.23.png'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('afroproplayer@gmail.com','zolaconnie@gmail.com', text)



