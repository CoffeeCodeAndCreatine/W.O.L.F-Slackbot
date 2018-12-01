import random

from utterances import cached_responses
from utterances import easter_eggs
from utterances import known_regexs
from utterances import known_utterances

from external_services import yafnag_integration
from external_services import pager_duty_integration
from external_services import github_integration


def known_utterance_handler(slack_client, message, channel):
    for entry in known_utterances.utterance_types:
        if entry.get("utterance") in message:
            message_string = get_utterance_response(message, entry.get("type"))
            slack_client.api_call("chat.postMessage", channel=channel, text=message_string)
            return


def get_utterance_response(message, utterance_type):
    if utterance_type == "help":
        return cached_responses.help_response
    if utterance_type == "pull_requests":
        return github_integration.get_github_info_message_string(message)
    if utterance_type == "support":
        return pager_duty_integration.get_pager_info_message_string(message)
    return ""


def known_regex_handler(slack_client, message, channel):
    for entry in known_regexs.known_regex_bases:
        if entry.get("base") in message:
            message_string = get_regex_response(message, entry.get("handler"))
            slack_client.api_call("chat.postMessage", channel=channel, text=message_string)
            return None


def get_regex_response(message, handler):
    if handler == "yafnag":
        return yafnag_integration.get_names_message_string(message)

def easter_egg_handler(slack_client, message, channel):
    slack_client.api_call("chat.postMessage", channel=channel, text=easter_eggs.easter_eggs.get(message))


def cached_response_handler(slack_client, channel):
    slack_client.api_call("chat.postMessage", channel=channel, text=cached_responses.confused[random.randrange(len(cached_responses.confused))])
