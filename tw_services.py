import requests
from _exceptions import ThoughtWorksException
from dotenv import load_dotenv
import os
import json

load_dotenv()

GAME_HOST = os.getenv("GAME_HOST")


def get_challenge_meta():
    challenge = requests.get('{}/challenge/input'.format(GAME_HOST), headers={
        'userId': os.getenv('user_id'),
        'Content-Type': 'application/json'
    })
    if challenge.status_code in range(199, 299):
        return json.loads(challenge.text)
    else:
        raise ThoughtWorksException(challenge.text)


def send_solution(solution):
    sol_response = requests.post('{}/challenge/output'.format(GAME_HOST),
                                 json=solution,
                                 headers={'userId': os.getenv('user_id'), 'Content-Type': 'application/json'})
    if sol_response.status_code in range(199, 299):
        print('Success', sol_response.text)
    else:
        raise ThoughtWorksException(sol_response.text)
