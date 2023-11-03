# Question: Create a script that generates a text file with all letters of the English alphabet inside it, one letter per line.
with open('my_letters.txt', 'w') as fd:
    fd.writelines([f'{chr(97+i)}\n' for i in range(0,26)])
    