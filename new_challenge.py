import requests
from _exceptions import ThoughtWorksException
from dotenv import load_dotenv
import os

load_dotenv()

GAME_HOST = os.getenv("GAME_HOST")


def get_new_challenge():
    challenge = requests.get('{}/challenge'.format(GAME_HOST), headers={
        'userId': os.getenv('user_id'),
        'Content-Type': 'application/json'
    })
    if challenge.status_code in range(199, 299):
        print('Challenge: ', challenge.text)
    else:
        raise ThoughtWorksException(challenge.text)
    return 1


if __name__ == '__main__':
    get_new_challenge()
