# Please download the file in the attachment and use Python to print out its content. file: company1.json
import json
with open('company1.json', 'r') as fp:
    contents = json.load(fp)
print(contents)