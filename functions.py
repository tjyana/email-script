# consolidate functions here
# connect everything in script.py

# functions needing to be created:
# get_daily_report()
# - add the pretrained model to generate text


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time
from transformers import GPT2Tokenizer, GPT2LMHeadModel


def get_daily_email():
    # Initialize the tokenizer and model
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    model = GPT2LMHeadModel.from_pretrained('gpt2')

    # Set the input text
    input_text = "What are some of the benefits of a good night's rest? Please return a different response each time."

    inputs = tokenizer(input_text, return_tensors="pt")

    attention_mask = inputs['attention_mask']

    # Generate text with additional parameters to reduce repetition
    output = model.generate(
        inputs['input_ids'],
        attention_mask=attention_mask,
        pad_token_id=tokenizer.eos_token_id,
        max_length=500,
        repetition_penalty=2.0,  # Penalty for repeating the same sequence
        top_k=50,  # Limits the sampling pool to the top k tokens
        top_p=0.95,  # Limits the sampling pool to the top p cumulative probability
        temperature=0.3,  # Controls randomness in the output
        num_return_sequences=1  # Number of sequences to generate
    )

    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    return generated_text
