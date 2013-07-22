import json
input_file_example = "input_data.json"

def read_input_data(input_file):
  with (open ("input_data.json")) as input_json_data
    input_data = json.loads(input_json_data)
  return input_data

def analyse_data (input_file):
  
  
  input_data = read_input_data(input_file)

  max_x = 0
  max_y = 0
  
  for var in input_data:
    if max_x < var["x"]:
      max_x = var["x"]
    if max_y < var["y"]:
      max_y =  var["y"]
   
  working_data = [{"real_sum": 0, "value_sum": 0, "check": False} for i in range(0,max_x)]      
  
  for var in input_data:
    working_data[i]["check"] = True    
    i = var["x"] - 1
    if var["y"] != max_y:
      working_data[i]["real_sum"]= working_data[i]["real_sum"] + var["value"]
    else:
      working_data[i]["value_sum"] = var["value"]
   
  result = [{"x": i+1, "correct": 0} for i in range(0,max_x)]
  i = 0
  for var in working_data:
    if var["check"] == False:
      del result[i]
    elif var["real_sum"] == var["value_sum"]:
      result[i]["correct"] = 1
      i = i + 1
    else:
      result[i]["correct"] = 0
      i = i + 1

  with open('output_file.txt', 'w') as output_file:
    json.dump(result, output_file) 
print analyse_data