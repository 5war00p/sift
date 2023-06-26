import sys
sys.path.append('..')

from sift.constants import email_providers

FREE_EMAIL_PROVIDERS = email_providers.FREE_EMAIL_PROVIDERS


def is_free(domain: str) -> bool:
    '''
        @param {domain: str} - a domain address
        @returns {bool}

        Verfies whether given email is provided by free email provders
    '''
    if domain in FREE_EMAIL_PROVIDERS:
        return True

    return False
