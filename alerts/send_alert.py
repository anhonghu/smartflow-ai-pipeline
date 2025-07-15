# alerts/send_alert.py

import smtplib
from email.mime.text import MIMEText
from config.load_config import load_config

def send_email_alert(subject, body):
    config = load_config()

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = config['smtp_user']
    msg['To'] = config['email_recipient']

    try:
        with smtplib.SMTP(config['smtp_server'], config['smtp_port']) as server:
            server.starttls()
            server.login(config['smtp_user'], config['smtp_password'])
            server.send_message(msg)
            print("📬 Alert sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send alert: {e}")