import re
import requests
import json

"""

Goal is to find the city of the Bank - Branch given an IFSC Code

Provider - RazorPay.
https://ifsc.razorpay.com/

Steps ->

1. Validate IFSC Code - standard regex
2. Get branch information from provider
   2.1 Success
   2.2 Failure
3. Presentation - Handling the response from the Provider

"""

IFSC_REGEX = "^[A-Z]{4}0[A-Z0-9]{6}$"

STANDARD_RESP = ['city', 'bank_name']


def is_valid_ifsc(ifsc):
    if not isinstance(ifsc, str):
        return False

    return bool(re.match(IFSC_REGEX, ifsc))


def fetch_branch_details_razorpay(ifsc):
    HOST = "https://ifsc.razorpay.com"

    try:
        resp = requests.get(url="{}/{}".format(HOST, ifsc))
    except Exception as e:
        raise Exception('Connection Error: {}'.format(e))

    if resp.status_code == 404:
        raise ValueError("Invalid IFSC")
    elif resp.status_code in range(499, 599):
        raise Exception("RazorPay Exception")
    elif resp.status_code == 200:
        # success
        rzp_bank_details = json.loads(resp.text)
        return rzp_bank_details['CITY']


def main(ifsc):
    if not is_valid_ifsc(ifsc=ifsc):
        print("Invalid IFSC")
    else:
        try:
            print(fetch_branch_details_razorpay(ifsc))
        except ValueError:
            print("Invalid IFSC")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main("KARB0000001")
