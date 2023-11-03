from io import TextIOWrapper
def num_of_words(fd: TextIOWrapper):
    lines = fd.readlines()
    words=0
    for line in lines:
        words+=len(line.split())
    return words

with open('words1.txt', 'r') as fd:
    print(num_of_words(fd))