import sys
import json


def load_json_file(filepath):
    with open(filepath, 'r', encoding="utf8") as file:
        list_to_print = json.load(file)
    return list_to_print


def pretty_print_json(data):
    print(json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4))


if __name__ == '__main__':
    filepath = sys.argv[1]
    list_to_print = load_json_file(filepath)
    pretty_print_json(list_to_print)
