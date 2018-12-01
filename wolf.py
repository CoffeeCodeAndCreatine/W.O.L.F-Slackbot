from slackeventsapi import SlackEventAdapter
from slackclient import SlackClient
from flask import Flask, jsonify
import re

from configs import config_loader
from secrets import secret_loader

from utterances import known_utterances
from utterances import easter_eggs
from utterances import known_regexs
from utterances import utterance_handler

from external_services import yafnag_integration

app = Flask(__name__)

wolf_slack_secrets = secret_loader.load_secrets().get("slack")
wolf_configs = config_loader.load_configs()
slack_events_adapter = SlackEventAdapter(wolf_slack_secrets.get("slack_signing_secret"), "/slack/events", app)
slack_client = SlackClient(wolf_slack_secrets.get("slack_bot_token"))
patterns = yafnag_integration.regex_compiler(known_regexs.known_regexs)


@app.route("/alive")
def alive():
    return jsonify({"health": "wolf is up and running"})


@app.route("/configs")
def configs():
    return jsonify(wolf_configs)


@slack_events_adapter.on("app_mention")  # subscribe to app mentions
@slack_events_adapter.on("message")  # subscribe to direct messages to bot
def handle_message(event_data):
    message = event_data["event"]
    channel = message["channel"]

    # Strip off the bot id from the message
    message_from_event = message.get('text')
    clean_message = re.sub(r'<@.........> ', '', message_from_event)

    # check to see if this is a direct match to an utterance we know how to handle
    if message.get("subtype") is None and clean_message in known_utterances.known_utterances:
        utterance_handler.known_utterance_handler(slack_client, clean_message, channel)

    # check to see if this is a direct match to an easter egg
    elif message.get("subtype") is None and clean_message in easter_eggs.easter_eggs and wolf_configs.get(
            "easter_eggs").get("enable"):
        utterance_handler.easter_egg_handler(slack_client, clean_message, channel)

    # check to see if this matches a reg ex, which will be a bit slower
    elif message.get("subtype") is None and re.match(patterns, clean_message):
        utterance_handler.known_regex_handler(slack_client, clean_message, channel)

    # return an "I dont know" response
    elif message.get("subtype") is None and wolf_configs.get("cached_response").get("enable"):
        utterance_handler.cached_response_handler(slack_client, channel)


@slack_events_adapter.on("error")
def error_handler(err):
    print("ERROR: " + str(err))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, use_reloader=False, threaded=True)
