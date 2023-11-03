file = open('97.txt', 'a+') 
while True:
    line = input("Enter value: ")
    if line == 'CLOSE':
        file.close()
        break
    if line == 'SAVE':
        file.close()
        file=open('97.txt', 'a+')
    else:
        file.write(line+'\n')
    