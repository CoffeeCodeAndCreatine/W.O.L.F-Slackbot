import json

def load_secrets():
    secrets = {}
    with open('secrets/master_secrets.json') as json_data:
        secrets = json.load(json_data)

    return secrets
