# Please download the attached urls.txt file. The file contains some broken URLs. Here's what the file contains:

# https:/www.google.com
# https:/www.yahoo.com
# https:/www.stackoverflow.com
# https:/www.pythonhow.com
# Please use Python to remove the "s" from "https" and add another forward slash next to the existing slash, so the content looks like in the expected output
with open('urls.txt', 'r') as f:
    urls = f.readlines()

urls = [url.replace('https', 'http') for url in urls]
urls = [url.replace(':/', '://') for url in urls]
print(urls)