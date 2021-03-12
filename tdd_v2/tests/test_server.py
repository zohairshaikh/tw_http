import requests
from flask import Flask
from tdd_v2.app import app
import json
from tdd_v2.consts import DOMAIN, PORT


def test_heartbeat():
    response = requests.get(url=DOMAIN)
    assert response.status_code == 200


def test_short_me():
    response = requests.post(url='{}/short_me/'.format(DOMAIN),
                             json=json.dumps({'long_url': 'wss://centrifugo.livehealth.solutions'}))
    assert response.status_code == 400
