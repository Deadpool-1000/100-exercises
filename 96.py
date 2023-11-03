# Ask for user input repeatedly and output the user input to text file
file = open('96.txt', 'w') 
while True:
    line = input("Enter value: ")
    if line == 'CLOSE':
        file.close()
        break
    else:
        file.write(line+'\n')
    