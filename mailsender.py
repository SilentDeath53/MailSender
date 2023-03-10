import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Establishing a connection to the SMTP server
smtp_server = 'smtp.gmail.com'
port = 587
smtp_username = 'your@gmail.com'
smtp_password = 'password'
smtp_connection = smtplib.SMTP(smtp_server, port)
smtp_connection.starttls()
smtp_connection.login(smtp_username, smtp_password)

# The addresses to which the message will be sent are determined
to_address = 'targetmail@gmail.com' # "targetmail@gmail.com, targetmail2@gmail.com"
from_address = 'from@gmail.com' # A Google acc that you want to set as a mailer

# Creating message content
message = MIMEMultipart()
message['From'] = from_address
message['To'] = to_address
message['Subject'] = 'Test Mail'

body = 'Hello, it is a test mail.'
message.attach(MIMEText(body, 'plain'))

# Message is sent via SMTP server
smtp_connection.sendmail(from_address, to_address, message.as_string())
smtp_connection.quit()
