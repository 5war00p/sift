import sys
sys.path.append('..')

import re
from sift.constants import regexp

EMAIL_PATTERN = regexp.EMAIL_PATTERN

def is_valid_email(email: str) -> bool:

    '''
        @param {email: str} - an email address
        @return {bool}

        Verifies whether an email address in obeying to the email address structure
        using Regular Expression
    '''

    if re.match(EMAIL_PATTERN, email):
        return True
    else:
        return False