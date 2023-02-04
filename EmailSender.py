from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'gd6noob@gmail.com'
email_password = 'ydragawoefheerwc'
email_receiver = 'mioradnw@hotmail.com'

subject = 'Miora, I miss you a lot'
body = '''Hello my love, \n
I miss you each and everyday. Sometimes I get mad or angry but I do not mean it in a bad way.\n
Thank you for accepting me for being me. \n \n
Also, I'm just testing my coding. '''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())