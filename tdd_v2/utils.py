import re
import random
import string
from tdd_v2.consts import DOMAIN


def validate_url(url):
    """
    given a URL -> matches it with the URL regex and returns a bool
    :param url: str
    :return: bool
    """
    HTTP_REGEX = '^((?:https?:\/\/)?[^./]+(?:\.[^./]+)+(?:\/.*)?)$'

    return bool(re.match(HTTP_REGEX, url))


def generate_short_url(long_url):
    """
    short_url = domain/redirect_api/short_url_id/
    :param long_url:
    :return:
    """

    letters = string.ascii_lowercase
    short_url_id = ''.join(random.choice(letters) for i in range(6))

    return '{}/{}/{}'.format(DOMAIN, 'redirect', short_url_id), short_url_id
