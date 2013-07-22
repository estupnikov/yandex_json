import json
import codecs
import urllib2
input_file_example = "input_data.json"

def read_input_data(encoding="cp1251"):
#    with (open ("generated.json")) as input_json_data:
#        input_data = json.loads(input_json_data)

    with codecs.open("generated.json","rt",encoding=encoding) as f:
        return json.load(f)

def from_http():
    r = urllib2.urlopen('http://www.oldieworld.com/input_data.json')

    return json.load(r)

#    with open("a.txt", "w") as f:
#        for item in json.load(r) or []:
#            try:
#                f.write(item['repository']['name'] + "\n")
#            except KeyError:
#                pass

#print read_input_data()
print from_http()