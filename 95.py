# Take input from user in comma seperated form and output data to file

data = input("Please enter values: ").split(',')

with open('95.txt', 'w') as f:
    f.writelines([f'{d}\n' for d in data])