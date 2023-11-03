# Question: Create a script that generates a file where all letters of the English alphabet are listed three in each line. 
with open('44.txt', 'w') as fd:
    fd.writelines([
        f'{chr(97+i)}{chr(98+i)}{chr(99+i)}\n'
        for i in range(0,26,3)
    ])


