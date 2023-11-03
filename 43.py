# Question: Create a script that generates a file where all letters of the English alphabet are listed two in each line. 
with open('43.txt', 'w') as fd:
    fd.writelines([f'{chr(97+i)}{chr(98+i)}\n' for i in range(0,25,2)])
