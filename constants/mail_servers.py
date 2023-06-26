
# ? Reference: https://support.google.com/mail/answer/7126229?hl=en#zippy=%2Cstep-check-that-imap-is-turned-on%2Cstep-change-smtp-other-settings-in-your-email-client
GOOGLE_EMAIL_SMTP_SERVERS = {
    # Require's Authentication
    0: {
        'address': 'smtp.gmail.com',
        'port': 587
    },

    ## Authentication not required
    1: {
        'address': 'gmail-smtp-in.l.google.com',
        'port': 25
    },
    2: {
        'address': 'alt1.gmail-smtp-in.l.google.com',
        'port': 25
    },
    3: {
        'address': 'alt2.gmail-smtp-in.l.google.com',
        'port': 25
    },
    4: {
        'address': 'alt3.gmail-smtp-in.l.google.com',
        'port': 25
    },
    5: {
        'address': 'alt4.gmail-smtp-in.l.google.com',
        'port': 25
    },
}

# ? https://support.microsoft.com/en-gb/office/pop-imap-and-smtp-settings-8361e398-8af4-4e97-b147-6c6c4ac95353
MICROSOFT_EMAIL_SMTP_SERVERS = {
    # Require's Authentication
    0: {
        'address': 'smtp.office365.com',
        'port': 587
    },
    1: {
        'address': 'smtp-mail.outlook.com',
        'port': 587
    }
}

# Like the above SMTP servers of any other providers can be added