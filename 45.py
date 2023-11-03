# Question: Please create a script that generates 26 text files named a.txt, b.txt, and so on up to z.txt. Each file should contain a letter reflecting its filename. So, a.txt will contain letter a, b.txt will contain letter b, and so on.

for i in range(0,26):
    with open(fr'C:\Users\mbhatnagar\OneDrive - WatchGuard Technologies Inc\Desktop\100-exercises\letters\{chr(97+i)}.txt', 'w') as fd:
        fd.writelines(chr(97+i))

