import json
import urllib2
input_http_example = "https://raw.github.com/estupnikov/yandex_json/master/input_data.json"

def read_input_data(input_http):
    read_data = urllib2.urlopen('input_http')

    return json.load(read_data)

def define_max_x_y (input_data):
    max_x = 0
    max_y = 0

    for var in input_data:
        if max_x < var["x"]:
            max_x = var["x"]
        if max_y < var["y"]:
            max_y =  var["y"]

    return {"max_x": max_x, "max_y": max_y}

def define_sum (input_data, max_x_y):
    working_data = [{"real_sum": 0, "value_sum": 0, "check": False} for i in range(0,max_x_y["max_x"])]

    for var in input_data:
        working_data[i]["check"] = True
    i = var["x"] - 1
    if var["y"] != max_x_y["max_y"]:
        working_data[i]["real_sum"]= working_data[i]["real_sum"] + var["value"]
    else:
        working_data[i]["value_sum"] = var["value"]

    return working_data

def check_correct (working_data, max_x_y):
    result = [{"x": i+1, "correct": 0} for i in range(0,max_x_y["max_x"])]
    i = 0
    for var in working_data:
        if var["check"] == False:
            del result[i]
        elif var["real_sum"] == var["value_sum"]:
            result[i]["correct"] = 1
            i =+ 1
        else:
            result[i]["correct"] = 0
            i =+ 1

    return result

def analyse_data (input_http):
    input_data = read_input_data(input_http)

    max_x_y = define_max_x_y(input_data)

    working_data = define_sum (input_data, max_x_y)

    result = check_correct (working_data, max_x_y)

    with open("output_file.txt", 'w') as output_file:
        json.dump(result, output_file)

analyse_data(input_http)