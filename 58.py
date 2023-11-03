# Question: Please download the json file in the attachment and use Python to add a new employee to the 
# file's content so that the file looks like in the expected output below.
import json

with open('company1.json', 'r') as fp:
    contents = json.load(fp)

with open('company1.json', 'w') as fp:
    contents["employees"].append({
        'firstName': 'Albert', 
        'lastName': 'Bert'
    })
    json.dump(contents, fp)


