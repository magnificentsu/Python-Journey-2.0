import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Magnificent Code'
email['to'] = 'sulei@magnificentsu.com'
email['subject'] = 'Just learned to send an email with Python'

email.set_content(html.substitute(name='Mrs. Random'), 'html')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('codewith24@gmail.com', 'ewtv gbdn ggem sgdf')
    smtp.send_message(email)
    print('Email sent')