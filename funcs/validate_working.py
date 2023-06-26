import sys
sys.path.append('..')

import smtplib
from sift.constants import mail_servers

GOOGLE_EMAIL_SERVER = mail_servers.GOOGLE_EMAIL_SMTP_SERVERS[1]

def is_email_working(sender_email: str, receiver_email: str) -> bool:
    '''
        @param {sender_email: str} - a sender email address
        @param {receiver_email: str} - a receiver email address
        @return {bool}

        Verifies whether an email address is working,
        i.e., accepting and responding to the emails

        Here we used one of the Google's SMTP server {mail_servers.GOOGLE_EMAIL_SMTP_SERVERS[1]}
        which doesn't require authorization. To work with secured SMTP servers one may need to add
        
        ```
            smtp_server.login(username, password)
        ```
        Refer: https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.login
    '''
    try:
        with smtplib.SMTP(GOOGLE_EMAIL_SERVER['address'], GOOGLE_EMAIL_SERVER['port']) as smtp_server:
            smtp_server.starttls()
            smtp_server.helo()

            # Simulate MAIL FROM and RCPT TO commands
            response = smtp_server.mail(sender_email)
            if response[0] == 250:
                response = smtp_server.rcpt(receiver_email)
                if response[0] == 250:
                    return True

        return False
    # Like the below, many individual exceptions can be handled differently based on use case
    except smtplib.SMTPException as e:
        print(e)
        return False
