'''
    HamsterCombat "Clicker", releasing people from hostage.

    The developers left no contacts, direct attempts at communication have failed.
    Many other more "serious" bugs remain unfixed.
    For an application preparing to issue tokens, this is not acceptable.

    (с) pwn-all.net | PWN-ALL Auditing, Reviewing & Testing Cyber Risks CO. L.L.C
'''

from random import randint
from time import time, sleep

from requests import Session
from requests.exceptions import Timeout, JSONDecodeError


class HamsterKombat:
    def __init__(self, bearer: str) -> None:
        self.ses = Session()
        self.ses.headers.update({
            'Accept': 'application/json',
            'Accept-Language': 'en-US',
            'Authorization': f'Bearer {bearer}',
            'Origin': 'https://hamsterkombat.io',
            'Referer': 'https://hamsterkombat.io/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15'
        })

    def clicker(self) -> None:
        '''
            Click, click, click, click
        '''

        allowed_taps = 2000

        while True:
            taps = randint(11, 592)
            data = {
                'count': taps,
                'availableTaps': allowed_taps-taps,
                'timestamp': int(time())
            }

            try:
                resp = self.ses.post(
                    'https://api.hamsterkombat.io/clicker/tap',
                    json=data,
                    timeout=15
                ).json()
            except (Timeout, JSONDecodeError):
                print('Error in process')
                break

            user = resp.get('clickerUser', {})
            coins = user.get('balanceCoins', -999)
            allowed_taps = user.get('availableTaps', -999)

            print(
                f'User Coins: {coins}', end='\r'
            )

            sleep(randint(1, 3))
