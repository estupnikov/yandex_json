import json
import urllib2
input_http_example = "https://raw.github.com/estupnikov/yandex_json/master/input_data.json"

def read_input_data(input_http):
    read_data = urllib2.urlopen(input_http)
    result = json.load(read_data)

    with open("output_file.json", 'w') as output_file:
        json.dump(result, output_file)

    return

print read_input_data(input_http_example)