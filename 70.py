# Question: Print out the text of this file https://pythonhow.com/media/data/universe.txt

# Don't manually download the file. Let Python do all the work.
import requests
data = requests.get('https://pythonhow.com/media/data/universe.txt').content
print(data)