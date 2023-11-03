# Question: Please download the attached ZIP file and extract its files in a folder. 
# Then, write a script that counts and 
# prints out the number of .py files in that folder.
import fnmatch
import os
dir_path = r'C:\Users\mbhatnagar\OneDrive - WatchGuard Technologies Inc\Desktop\100-exercises\count_files' 
count = len(fnmatch.filter(os.listdir(dir_path), '*.py'))
print('File Count:', count)