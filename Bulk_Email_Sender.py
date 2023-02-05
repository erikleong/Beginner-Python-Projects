import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Start smtp server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("username", "password")

# Read data from csv file
with open('bulk_email.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Skip header
    next(csv_reader)

    # Send emails
    for row in csv_reader:
        recipient = row[0]
        sender = row[1]
        subject = row[2]
        body = row[3]
        attachment1 = row[4]
        attachment2 = row[5]

        # Create message
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = recipient
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Attach files
        if attachment1 != '':
            message.attach(attachment1)
        if attachment2 != '':
            message.attach(attachment2)

        # Send email
        server.send_message(message)

# Close server
server.quit()