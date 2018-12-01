import requests

from configs import config_loader
from secrets import secret_loader


def get_pager_info_message_string(message):
    pager_secrets = secret_loader.load_secrets().get("pager_duty")
    usernames = get_pager_usernames(pager_secrets.get("pager_duty_token"), pager_secrets.get("pager_duty_primary_ids"), pager_secrets.get("pager_duty_secondary_ids"))
    message_string = "Here are the users currently on support:\n```\n"
    message_string = message_string + "Primary support: " + usernames.get("primary") + "\nSecondary support: " + usernames.get("secondary")
    message_string = message_string + "\n```"
    return message_string


def get_pager_usernames(token, primary_ids, secondary_ids):
    pager_configs = config_loader.load_configs().get("pager_duty")

    pager_duty_headers = {
        "Authorization": pager_configs.get("authorization_prefix") + token,
        "Accept": pager_configs.get("accept_type")
    }
    pager_duty_url = pager_configs.get("base_url")

    primary = ""
    seconday = ""

    primary_request = requests.get(pager_duty_url.format(primary_ids[0], primary_ids[1]), headers=pager_duty_headers)
    secondary_requests = requests.get(pager_duty_url.format(secondary_ids[0], secondary_ids[1]), headers=pager_duty_headers)

    if primary_request.status_code != 200:
        primary = "No primary contact found"
    else:
        respObj = primary_request.json()
        primary = respObj["oncalls"][0]["user"]['email'].split("@")[0]

    if secondary_requests.status_code != 200:
        seconday = "No secondary contact found"
    else:
        respObj = secondary_requests.json()
        seconday = respObj["oncalls"][0]["user"]['email'].split("@")[0]

    pager_wrapper = {}
    pager_wrapper["primary"] = primary
    pager_wrapper["secondary"] = seconday
    return pager_wrapper