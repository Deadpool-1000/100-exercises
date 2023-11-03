# Question: Please download the attached ZIP file. Inside the ZIP file, t
# here's a directory named subdirs. 
# That directory contains other directories inside. 
# Please write a script that counts the number of .py files 
# contained inside subdirs and all its sub-directories.
import glob
 
file_list = glob.glob("count_files/subdirs/**/*.py", recursive=True)
print(len(file_list))

