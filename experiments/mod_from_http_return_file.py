import json
import urllib2

# URL for input json-data

input_http_example = "https://raw.github.com/estupnikov/yandex_json/master/project/input_data.json"

# Load json-data

def read_input_data(input_http):
    read_data = urllib2.urlopen(input_http)

    return json.load(read_data)

# Define table size

def define_max_x_y (input_data):
    max_x = 0
    max_y = 0

    for var in input_data:
        if max_x < var["x"]:
            max_x = var["x"]
        if max_y < var["y"]:
            max_y =  var["y"]

    return {"max_x": max_x, "max_y": max_y}

# Define real sum for each column and data in last row.

def define_sum (input_data, max_x_y):
    working_data = [{"real_sum": 0, "value_sum": 0, "check": False} for i in range(0,max_x_y["max_x"])]

    for var in input_data:
        working_data[i]["check"] = True # Set flag if any data in column
        i = var["x"] - 1
        if var["y"] != max_x_y["max_y"]:
            working_data[i]["real_sum"]= working_data[i]["real_sum"] + var["value"] # Define real sum for each column
        else:
            working_data[i]["value_sum"] = var["value"] # Define data in last row

    return working_data

# Check if sum for each column in provided data correct

def check_correct (working_data, max_x_y):
    result = [{"x": i+1, "correct": 0} for i in range(0,max_x_y["max_x"])]
    i = 0
    for var in working_data:
        if var["check"] == False: # Check if any data in column
            del result[i]
        elif var["real_sum"] == var["value_sum"]: # Check correctnes
            result[i]["correct"] = 1
            i =+ 1
        else:
            result[i]["correct"] = 0
            i =+ 1

    return result

# Define if sum of the numbers in each column in input table is equal to an appropriate value in the last row

def analyse_data (input_http):
    input_data = read_input_data(input_http) # Load data

    max_x_y = define_max_x_y(input_data) # Define table size

    working_data = define_sum (input_data, max_x_y) # Define real sum for each column and data in last row.

    result = check_correct (working_data, max_x_y) # Check if sum for each column in provided data correct

    return str(result) # Return result
#    with open("output_file.json", 'w') as output_file: # Pack result in json-file
#        json.dump(result, output_file)

print analyse_data(input_http_example)