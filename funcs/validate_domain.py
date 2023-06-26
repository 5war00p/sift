import dns.resolver

def is_valid_domain(domain: str) -> bool:
    '''
        @param {domain: str} - a domain address
        @return {bool}

        Verfies whether given domain is valid or not
        by checking Mail Exchangeg(MX) records
    '''

    try:
        # Query the DNS for the domain's MX (Mail Exchange) records
        mx_records = dns.resolver.resolve(domain, 'MX')
        if mx_records:
            return True
    
    # Like the below, many individual exceptions can be handled differently based on use case
    except dns.resolver.NoAnswer as e:
        print(e)
        return False
    except dns.resolver.NXDOMAIN as e:
        print(e)
        return False
    
    return False