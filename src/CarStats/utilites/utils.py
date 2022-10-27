"""
Helpfull tools
"""
import json


def check(name, select, *options):
    """Check if a select is in the list of options. If not raise ValueError

    **Arguments:**

    name
         The name of the argument.

    select
         The value of the argument.

    options
         A list of allowed options.
    """
    if select not in options:
        formatted = ", ".join([f"'{option}'" for option in options])
        raise ValueError(f"The argument '{name}' must be one of: {formatted}")


def export_to_json(data):
    """convert dict to json"""
    json_string = json.dumps(data, ensure_ascii=False).encode("utf8")
    return json_string


def dump(data, filename="scraped.json"):
    """dump to file"""
    with open(f"{filename}", "w", encoding="utf-8") as file:
        json.dump(data.decode(), file, ensure_ascii=False)
