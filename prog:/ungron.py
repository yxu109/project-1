import json
import re

def ungron(input_lines):
    data = {}

    for line in input_lines:
        # Remove trailing semicolon and whitespace
        line = line.strip().strip(';')

        # Skip empty lines
        if not line:
            continue

        # Split path and value
        path, value = re.match(r'^(.*?) = (.*)$', line).groups()

        # Process the path and value
        keys = path.split('.')
        current = data

        for i, key in enumerate(keys):
            if key == "json":
                continue

            # Check for array index
            array_match = re.match(r'(.*)\[(\d+)\]$', key)
            if array_match:
                key, index = array_match.groups()
                index = int(index)

                if key not in current:
                    current[key] = []

                # Extend the array if necessary
                while len(current[key]) <= index:
                    current[key].append({})

                if i == len(keys) - 1:
                    current[key][index] = parse_value(value)
                else:
                    current = current[key][index]
            else:
                if i == len(keys) - 1:
                    current[key] = parse_value(value)
                else:
                    current = current.setdefault(key, {})

    return data

def parse_value(value):
    # Convert the value from string to appropriate type
    if value.startswith('"') and value.endswith('"'):
        return value.strip('"').replace('\\"', '"')
    elif value == "{}":
        return {}
    elif value == "[]":
        return []
    elif value == "true":
        return True
    elif value == "false":
        return False
    elif value.replace('.', '', 1).isdigit():
        return float(value) if '.' in value else int(value)
    else:
        return value  # As is, for anything else

def main():
    try:
        import sys
        filename = sys.argv[1]

        with open(filename, 'r') as file:
            input_lines = file.readlines()
    except IndexError:
        # If no file is provided, read from STDIN
        print("Reading from STDIN. Enter your flattened JSON and press Ctrl-D:")
        input_lines = sys.stdin.readlines()

    original_json = ungron(input_lines)
    print(json.dumps(original_json, indent=2))

if __name__ == "__main__":
    main()
