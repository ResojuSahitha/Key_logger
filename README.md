# Key_logger
This is a simple Python-based keylogger project that captures keystrokes and saves them to a file, and sends the logged keystrokes via email. It uses the pynput library to listen for keystrokes and smtplib for sending emails securely over TLS.

Project Features:
Keystroke Logging:

Listens to and logs every keystroke made by the user.
Special keys like Enter, Backspace, and Tab are identified and logged appropriately.
File Writing:

Keystrokes are appended to a text file keylogger.txt during the program’s execution.
Sending Logs via Email:

Once the keylogger stops (by pressing the Escape key), the contents of the log file are sent to the specified email address using the SMTP protocol.
Secure connection is established using TLS (Transport Layer Security).
Cross-Platform:

Works on Windows, macOS, and Linux.
Requirements:
Python 3.x installed on your machine.
Necessary libraries installed:
bash
Copy code
pip install pynput
How It Works:
The keylogger listens for every keystroke and writes it to a file (keylogger.txt).
Once the user presses Escape, the listener stops, and the log file is automatically emailed to a predefined email address.
How to Use:
Clone the Repository:

bash
Copy code
git clone https://github.com/your_username/keylogger-python.git
Install Required Libraries:

bash
Copy code
pip install pynput
Set Up Email Credentials:

Open the Python script and replace the sender_mail, receiver_mail, and password variables with your email credentials.
For Gmail users, you may need to enable "Less Secure Apps" or use an App-Specific Password.
Run the Script:

bash
Copy code
python keylogger.py
Stop the Keylogger:

Press Escape (Esc) to stop logging, which will also trigger sending the logs via email.
Disclaimer:
This project is intended for educational purposes only. It should be used ethically and legally, with proper authorization from system owners. Unauthorized use of keyloggers can violate privacy and security laws, and may result in severe penalties.

