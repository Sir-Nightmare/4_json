import json


def load_data(filepath):
    data = ""
    with open(filepath, 'r', encoding="utf8") as file:
        data = file.read()
    return json.loads(data)


def pretty_print_json(data):
    '''
    God bless python documentation! :D
    '''
    print(json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4))


if __name__ == '__main__':
    data = load_data('alco_shops.json')
    data = load_data(input('Type the path to json file'))
    pretty_print_json(data)
