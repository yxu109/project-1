import json
import sys
import argparse

def flatten_json(data, base_obj_name='json', parent_key=''):
    """
    Recursively flattens a JSON object and returns its paths as strings.
    """
    items = []
    if isinstance(data, dict):
        for k, v in data.items():
            new_key = f"{parent_key}.{k}" if parent_key else f"{base_obj_name}.{k}"
            items.extend(flatten_json(v, base_obj_name, new_key))
    elif isinstance(data, list):
        for i, v in enumerate(data):
            new_key = f"{parent_key}[{i}]"
            items.extend(flatten_json(v, base_obj_name, new_key))
    else:
        items.append(f"{parent_key} = {json.dumps(data)}")
    return items

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument("--obj", default="json")
    args = parser.parse_args()

    data = json.load(args.file)
    flattened_data = flatten_json(data, base_obj_name=args.obj)
    for item in flattened_data:
        print(item)

if __name__ == "__main__":
    main()
