
import pytest
from tdd_v2.utils import validate_url

def test_validate_url():

    assert validate_url('random string') == False
    assert validate_url('wss://centrifugo.livehealth.solutions') == False

    assert validate_url('http://livehealth.solutions') == True
    assert validate_url('https://livehealth.solutions') == True





