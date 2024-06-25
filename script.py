import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Configuration
SMTP_SERVER = 'smtp.gmail.com'  # e.g., 'smtp.gmail.com' for Gmail
SMTP_PORT = 587  # Typically 587 for TLS, 465 for SSL
EMAIL_ADDRESS = 'REDACTED'
EMAIL_PASSWORD = 'REDACTED'

TO_ADDRESS = 'REDACTED'
SUBJECT = '[TESTING] Daily Report from the script'



##### original function
# def get_daily_report():
#     # Replace this function with actual report generation logic
#     return "Here is your daily report."


# returns stuff but...params need adjusting.
# - occasional weirdness in the output
# - repetition of the same output
def get_daily_report():

    # Initialize the tokenizer and model
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    model = GPT2LMHeadModel.from_pretrained('gpt2')

    # Set the input text
    input_text = "Sleep is important for good physical and mental health. One specific benefit of sleep is: "

    inputs = tokenizer(input_text, return_tensors="pt")

    attention_mask = inputs['attention_mask']

    # Generate text with additional parameters to reduce repetition
    output = model.generate(
        inputs['input_ids'],
        attention_mask=attention_mask,
        pad_token_id=tokenizer.eos_token_id,
        max_length=200,
        repetition_penalty=2.0,  # Penalty for repeating the same sequence
        top_k=50,  # Limits the sampling pool to the top k tokens
        top_p=0.5,  # Limits the sampling pool to the top p cumulative probability
        temperature=0.7,  # Controls randomness in the output
        num_return_sequences=1,  # Number of sequences to generate
        do_sample=True
    )

    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    return generated_text

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

job()

# Uncomment below for scheduling
# ----------------------------------------------
# # Schedule the job every day at a specific time (e.g., 8:00 AM)
# schedule.every().day.at("10:24").do(job)

# # Keep the script running
# while True:
#     schedule.run_pending()
#     time.sleep(1)
# ----------------------------------------------
