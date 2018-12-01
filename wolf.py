from slackeventsapi import SlackEventAdapter
from slackclient import SlackClient
from flask import Flask, jsonify

from configs import config_loader
from secrets import secret_loader

app = Flask(__name__)

wolf_configs = config_loader.load_configs()
wolf_secrets = secret_loader.load_secrets()

slack_events_adapter = SlackEventAdapter(wolf_secrets.get("slack_signing_secret"), "/slack/events", app)
slack_client = SlackClient(wolf_secrets.get("slack_bot_token"))


@app.route("/alive")
def alive():
    return jsonify({"health": "wolf is up and running"})

@app.route("/configs")
def configs():
    return jsonify(wolf_configs)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, use_reloader=False, threaded=True)
