import sys
sys.path.append('..')

from sift.funcs import validate_email, validate_domain, validate_tld, validate_working, validate_role, validate_free, validate_disposability
from sift.utils import email_split


def examine(sender_email: str, receiver_email: str) -> dict[str, str | bool | dict[str, bool]]:
    '''
        @param {sender_email: str} - sender email address
        @param {receiver_email: str} - receiver email address
        @return {dict[str, str | bool | dict[str, str]]}

        Inspects email address and returns validity, along with extras [is_free is_disposable, is_role_specific]
    '''

    is_valid_email = bool(validate_email.is_valid_email(receiver_email))

    email_data = email_split.split(receiver_email)
    username = email_data['username']
    domain = email_data['domain']['address']
    tld = email_data['tld']

    is_valid_domain = bool(validate_domain.is_valid_domain(domain))
    is_valid_tld = bool(validate_tld.is_valid_tld(tld))
    is_working = bool(validate_working.is_email_working(sender_email, receiver_email))

    is_valid = is_valid_email and is_valid_domain and is_valid_tld and is_working

    is_role_specific = bool(validate_role.is_role_specific(username))
    is_free = bool(validate_free.is_free(domain))
    is_disposabale = bool(validate_disposability.is_disposable(domain))

    return dict({
        'email': receiver_email,
        'is_valid': is_valid,
        'extras': dict({
            'is_role_specific': is_role_specific,
            'is_free': is_free,
            'is_disposabale': is_disposabale
        })
    })

def examine_addresses(sender_email: str, receivers: list[str]) -> list[dict[str, str | bool | dict[str, bool]]]:
    '''
        @param {sender_email: str} - sender email address
        @param {receivers: list[str]} - a list of receiver email addresses
        @return {list[dict[str, str | dict[str, str]]]}

        Inspects list of email address and returns validity, along with extras [is_free is_disposable, is_role_specific]
    '''

    data = []
    filtered_receivers = list(set(filter(None, receivers)))

    for receiver_email in filtered_receivers:
        response = examine(sender_email, receiver_email)
        data.append(response)

    return data
