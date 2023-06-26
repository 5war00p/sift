import sys
sys.path.append('..')

import dns.resolver
from sift.utils import request_tlds

def is_valid_tld(tld: str) -> bool:
    '''
        @param {tld: str} - a TLD (Top-Level Domain)
        @return {bool}

        Verfies TLD with IANA TLD list and queries for DNS Name Server (NS) records 
    '''
    tld_uppercased = tld.upper()
    iana_tld_list = request_tlds.get_tld_list()
    is_tld_exists_in_iana = tld.upper() in iana_tld_list

    try:
        if not is_tld_exists_in_iana:
            return False
        # Query the DNS for the TLD's NS (Name Server) records
        ns_records = dns.resolver.resolve(tld_uppercased, 'NS')
        if ns_records:
            return True
    except dns.resolver.NXDOMAIN:
        return False

    return False