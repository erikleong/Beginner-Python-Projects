from email.message import EmailMessage
import ssl
import smtplib

email_sender = '@gmail.com'
email_password = ''
email_receiver = '@hotmail.com'

subject = 'Subject Line'
body = '''Hello, \n
Testing line 1.\n
Testing line 2. \n \n
Testing line 3. '''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
