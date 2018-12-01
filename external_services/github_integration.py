import requests

from configs import config_loader
from secrets import secret_loader


def get_github_info_message_string(message):
    message_string = ""
    pull_request_list = []

    if "approved" in message:
        pull_request_list = get_pull_requests("approved")
        message_string = "I have found " + str(len(pull_request_list)) + " approved pull requests"
    elif "open" in message:
        pull_request_list = get_pull_requests("open")
        message_string = "I have found " + str(len(pull_request_list)) + " open pull requests"
    else:
        pull_request_list = get_pull_requests("all")
        message_string = "I have found " + str(len(pull_request_list)) + " pull requests"

    if len(pull_request_list) > 0:
        message_string = message_string + "\n```"
        for pull_request in pull_request_list:
            message_string = message_string + pull_request.get("user") + ": " + pull_request.get("url") + "\n"

        message_string = message_string + "\n```"
    return message_string


def get_pull_requests(type):
    github_configs = config_loader.load_configs().get("github")
    github_secrets = secret_loader.load_secrets().get("github")

    response_json = []
    headers = {"Authorization": github_secrets.get("github_token")}
    for repo in github_configs.get("github_repos"):
        url_string = github_configs.get("base_url") + github_configs.get(
            "github_org") + "/" + repo + github_configs.get("tail_url")
        resp = requests.get(url_string, headers=headers, verify=False)
        repo_pulls = resp.json()
        for repo_pull in repo_pulls:
            temp_json = {
                "title": repo_pull['title'],
                "user": repo_pull['user']['login'],
                "repo": repo,
                "url": repo_pull['html_url'],
                "approved": get_pull_request_status(github_secrets.get("github_token"), repo_pull['url'])
            }

            if type == "approved" and temp_json.get("approved"):
                response_json.append(temp_json)
            elif type == "open" and not temp_json.get("approved"):
                response_json.append(temp_json)
            else:
                response_json.append(temp_json)

    return response_json


def get_pull_request_status(git_hub_token, url):
    headers = {"Authorization": git_hub_token}
    url_string = url + "/reviews"
    resp = requests.get(url_string, headers=headers, verify=False)
    resp_json = resp.json()
    if len(resp_json) > 0:
        state = resp_json[0].get("state")
        if state == "APPROVED":
            return True
        else:
            return False
    return False
