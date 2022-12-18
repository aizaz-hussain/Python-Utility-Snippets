import json
absJsonConfigPath = './sample.json'
pathDelimiter = '.'

with open(absJsonConfigPath, "r") as jsonFile:
    data = json.load(jsonFile)

def get_value(path):
    keys = path.split(pathDelimiter)
    rv = data
    for key in keys:
        rv = rv[key]
    return rv

def update_value(d, path, value):
    out = path.split(pathDelimiter, 1)
    key = out[0]
    if len(out) > 1:
        path = out[1]
        return update_value(d[key], path, value)
    else:
        d[key] = value

def update_json(path, value):
    update_value(data, path, value)
    with open(absJsonConfigPath, "w") as jsonFile:
        json.dump(data, jsonFile, indent=4, separators=(',', ': '))