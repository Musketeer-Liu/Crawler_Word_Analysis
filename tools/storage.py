import json




def file_to_set(filename):
    results = set()
    with open(filename, 'rt') as file:
        for line in file:
            results.add(line.replace('\n', ''))
    return results


def set_to_file(filename):
    with open(filename, 'r') as file:
        data = json.loads(file)
    return data