import json


data = [
    {"jmeno": "Alice", "vek":20},
    {"jmeno": "Bob", "vek":21},
    {"jmeno": "dave", "vek":25},
]



if __name__ == "__main__":

    data[2]["vek"] = 31
    data.append({"jmeno": "Monika", "vek": 28})

    json_data = json.dumps(data)

    print(json_data)
    with open("data.json", "w") as fp:
        fp.write(json_data)