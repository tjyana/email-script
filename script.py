import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

# Configuration
SMTP_SERVER = 'smtp.gmail.com'  # e.g., 'smtp.gmail.com' for Gmail
SMTP_PORT = 587  # Typically 587 for TLS, 465 for SSL
EMAIL_ADDRESS = 'EMAIL'
EMAIL_PASSWORD = 'PASSWORD'

TO_ADDRESS = 'EMAIL'
SUBJECT = '[TESTING] Daily Report from the script'

def get_daily_report():
    # Replace this function with actual report generation logic
    return "Here is your daily report."

def send_email(subject, body, to_address):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_address
    msg['Subject'] = subject

    # Attach the email body to the message
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Log in to the email account
            server.sendmail(EMAIL_ADDRESS, to_address, msg.as_string())  # Send the email
        print('Email sent successfully')
    except Exception as e:
        print(f'Failed to send email: {e}')

def job():
    report = get_daily_report()  # Generate the report
    send_email(SUBJECT, report, TO_ADDRESS)  # Send the email

# Schedule the job every day at a specific time (e.g., 8:00 AM)
schedule.every().day.at("10:24").do(job)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
