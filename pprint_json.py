import sys
import json


def load_json_file(filepath):
    with open(filepath, 'r', encoding="utf8") as file:
        json_content = json.load(file)
    return json_content


def pretty_print_json(data):
    print(json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4))


if __name__ == '__main__':
    filepath = sys.argv[1]
    pretty_print_json(load_json_file(filepath))
