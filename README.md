# slackbot_wolf_bot
WOLF: Work Organizing Lite Framework

## Main Features
1. Pull a list of open and or approved pull requests for a given git organization.
2. Pull the primary and secondary support individuals via a pager duty integration
3. Pull a list of randomly generated names from yafnag  

## Explanation of Files
1. /configs/master_config.json: Configs file for bot
2. /secrets/master_secrets.json: Secrets file for bot

## How to Configure the slackbot_wolf_bot
In order for this bot to run, you are going to need to fill out the blank fields in the configs and secrets files listed above

Configs
```bash
{
  "github": {
    "github_repos": [],
    "github_org": "",
  }
}
```
Secrets
```bash
{
  "slack": {
    "slack_bot_token": "This is the token of the bot user",
    "slack_signing_secret": "This is the signing secret of the app's event subscription"
  },
  "github": {
    "github_token": "This is a developer app token for git"
  },
  "pager_duty": {
    "pager_duty_token": "This is a auth token for pager duty",
    "pager_duty_primary_ids": ["This is an array of ids for primary on callers"],
    "pager_duty_secondary_ids": ["This is an array of ids for secondary on callers"]
  }
}
```

## How to Run
At a high level, the steps you will need to take to get this set up are listed below. If you want a more comprehensive walk through, please check out the youtube link below. 

1. Create an application in slack
2. Add a bot user to the slack application
3. Enable OAuth for the bot user
4. Grant the bot user chat:write:bot scope
5. Enable event subscriptions
6. Grant the subscribe to bot events the message.channels scope
7. Copy the slack bot token and the slack signing secret to the configs.json file
8. In terminal session a, launch ngrok 
    ```bash
    ./ngrok http 3000
    ```
9. In terminal session b, launch the slack bot
    ```bash
    pip3 install -r requirements.txt
    python3 slackbot_events_api_example.py
    ```
10. Now you should be able to go to the slack app, invite the bot and then send a message
    ```bash
    /invite @slackbot_events_api_example
    @slackbot_events_api_example BOT TEST
    ```
11. If everything went to play the bot should respond with the following
    ```bash
    Responding to `BOT TEST` message sent by user @yourUserName
    ```


## How To Video
[Coming Soon]()