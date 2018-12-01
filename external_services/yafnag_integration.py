import requests

from configs import config_loader


def regex_compiler(regs):
    return "(" + ")|(".join(regs) + ")"


def get_names_message_string(message):
    names_list = get_names(message)
    message_string = "Here is the list of names:\n```\n"
    for name in names_list:
        message_string = message_string + "\t" + name + "\n"

    message_string = message_string + "```"
    return message_string


def get_names(message):
    words = message.split(" ")
    number_of_names = words[0]
    first_letter_of_names = words[1]

    if number_of_names > 10:
        number_of_names == 10

    return yafnag_rest_call(first_letter_of_names, number_of_names)


def yafnag_rest_call(first_letter, number_of_names):
    yafnag_configs = config_loader.load_configs().get("yafnag")

    data = [
        ('pmin', yafnag_configs.get("min_character_count")),
        ('pmax', yafnag_configs.get("max_character_count")),
        ('qte', number_of_names),
        ('first', first_letter),
        ('oks', ''),
        ('lg', 'e'),
        ('_', ''),
    ]

    response_json = requests.post(yafnag_configs.get("base_url"), data=data).json()
    names = parse_yafnag_response(response_json)
    return names


def parse_yafnag_response(yafnag_json):
    res_string = yafnag_json["resu"]
    res_string = res_string.replace('<br>', '')
    res_string = res_string.replace('</p>', '')
    res_string = res_string.replace('<h3>Results:</h3>', '')
    res_string = res_string.replace('<p class="biglist">', '')
    res_string = res_string.strip()
    names = res_string.split("\n")
    return names