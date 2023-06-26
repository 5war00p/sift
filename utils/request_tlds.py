
import requests
import sys
sys.path.append('..')
from sift.constants import urls


def get_tld_list() -> list[str]:
    """ 
        @return {list[str]}

        Gives a list of TLDs from IANA URL\n
        https://data.iana.org/TLD/tlds-alpha-by-domain.txt

        Optionally one can use {tldextract} module which is available in PyPI
        Anyway this does the same
    """
    response = requests.get(urls.IANA_TLD_LIST_URL)
    tld_list = response.text.split('\n')[1:-1]
    return tld_list
