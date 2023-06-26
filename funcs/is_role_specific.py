import sys
sys.path.append('..')

from sift.constants import roles

ROLE_PREFIXES = roles.ROLE_PREFIXES

def is_role_specific(username: str):
    ''' 
        @param {email: str} - a username (local-part)
        @return {bool}

        To detect whether a given email address seems
        role specific or not
    '''

    # local_part = email.split('@')[0]
    # prefix = local_part.lower()

    if username in ROLE_PREFIXES:
        return True

    return False