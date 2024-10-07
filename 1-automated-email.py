import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

# Check environment variable
email_password = os.getenv('GMAIL_APP_PASSWORD')
print(f"Email Password Loaded: {bool(email_password)}")  # Check if password is loaded

smtp_server = 'smtp.gmail.com'
port = 587
sender_email = 'dipeshghimire.dg@gmail.com'
receiver_email = 'dipeshghimire.dg@gmail.com'

msg = MIMEText("Hello This is an automated message.")
msg['Subject'] = 'Python Automated Email'
msg['From'] = sender_email
msg['To'] = receiver_email

try:
    with smtplib.SMTP(smtp_server, port, timeout=10) as server:
        print("Connecting to server...")
        server.starttls()
        print("Starting TLS...")
        server.login(sender_email, email_password)
        print("Login successful...")
        server.sendmail(sender_email, [receiver_email], msg.as_string())
        print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")