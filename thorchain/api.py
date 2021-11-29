import requests

api_url = 'https://testnet.midgard.thorchain.info/v2/'
member_url = 'member/'


def is_pool_participant(user):
    return requests.get(api_url + member_url + str(user.user_id)).status_code != 404


def get_member_details(user):
    response = requests.get(api_url + member_url + str(user.user_id))
    if response.status_code != 404:
        return response.json()
