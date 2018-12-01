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
6. Grant the subscribe to bot events the app_mention and message.im scope
7. Configure the configs ans secrets files
8. In terminal session a, launch ngrok 
    ```bash
    ./ngrok http 3000
    ```
9. In terminal session b, launch the slack bot
    ```bash
    pip3 install -r requirements.txt
    python3 wolf.py
    ```
10. Now you should be able to go to the slack app, invite the bot and then send a message
    ```bash
    /invite @wolf
    @wolf help
    ```
11. If everything went to plan the bot should respond with the following
    ```bash
        I am The Slack Wolf. Here to help with little tasks here and there, but doing my best to stay our of your way. Right now I have a few commands I can answer to. They are as follows:

        help: I'll give you a list of things I can do.
        pr list: I'll give you a list of all open pull requests.
        approved pr list: I'll give you a list of all open pull requests that have been approved.
        open pr list: I'll give you a list of all open pull requests that have not been approved.
        pager duty: I'll tell you who is primary and secondary on call for the Ranking team.
        X Y names please: Random name generator, X is the amount of names, Y is the first letter.

        Thanks for reading, as of now that is all I can do, but if you would like me to learn something new please reach out to handler.
    ```


## How To Video
[Coming Soon]()