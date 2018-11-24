import json


def load_configs_from_file():
    settings = {}
    with open('configuration_files/master_config.json') as json_data:
        settings = json.load(json_data)
    return settings


def main():

    settings_json = load_configs_from_file()
    print(settings_json)


if __name__ == '__main__':
    main()