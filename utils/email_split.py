def split(email: str) -> dict[str, str | dict[str, str]]:
    '''
        @param {email: str} - an email address
        @return {dict[str, str | dict[str, str]]}

        Splits email into parts and gives required data
    '''
    local_part, domain = email.split('@')
    domain_name, tld = domain.split('.')

    return dict({
        'username': local_part,
        'domain': dict({
            'name': domain_name,
            'address': domain
        }),
        'tld': tld
    })