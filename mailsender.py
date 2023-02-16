import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP sunucusuna bağlantı kuruluyor
smtp_server = 'smtp.gmail.com'
port = 587
smtp_username = 'your@gmail.com'
smtp_password = 'password'
smtp_connection = smtplib.SMTP(smtp_server, port)
smtp_connection.starttls()
smtp_connection.login(smtp_username, smtp_password)

# Mesajın gönderileceği adresler belirleniyor
to_address = 'targetmail@gmail.com'
from_address = 'from@gmail.com'

# Mesaj içeriği oluşturuluyor
message = MIMEMultipart()
message['From'] = from_address
message['To'] = to_address
message['Subject'] = 'Test Mail'

body = 'Hello, it is a test mail.'
message.attach(MIMEText(body, 'plain'))

# Mesaj SMTP sunucusu üzerinden gönderiliyor
smtp_connection.sendmail(from_address, to_address, message.as_string())
smtp_connection.quit()
