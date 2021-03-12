from flask import Flask, request
from tdd_v2.queries.Urls import Urls
from tdd_v2.utils import validate_url, generate_short_url
import json

app = Flask(__name__)

URLS = Urls()


@app.route('/short_me/', methods=['POST'])
def short_me():
    body = json.loads(request.get_json())
    print(body)
    long_url = body.get('long_url', None)

    if not validate_url(long_url):
        return "Invalid request", 400

    short_url, short_url_id = generate_short_url(long_url)

    return "Success"


@app.route('/redirect/<short_url>', methods=['GET'])
def redirect(short_url):


    return "Success"



@app.route('/')
def heartbeat():
    pass

    return "Success"


if __name__ == '__main__':
    app.run(port=8011)
