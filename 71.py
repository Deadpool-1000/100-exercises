# Count the number of "a" characters in this text file: http://www.pythonhow.com/data/universe.txt
import requests
data = requests.get('https://pythonhow.com/media/data/universe.txt').text
print(data.count('a'))