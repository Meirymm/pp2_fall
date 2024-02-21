import json

# Load the JSON data from the file
with open('sample-data.json') as file:
    data = json.load(file)

# Iterate over each item in the JSON data
for item in data:
    print("ID:", item['adminSt'])
                    
    

