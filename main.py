import os
from dotenv import load_dotenv

# Local imports
from utils import examine

load_dotenv()

SENDER_EMAIL = str(os.getenv('SENDER_EMAIL'))


if __name__ == '__main__':
    # Test
    receivers = ['tahihad877@extemer.com', 'support@apilayer.com', 'xoxox@popo.in']
    data = examine.examine_addresses(SENDER_EMAIL, receivers)
    print(data)