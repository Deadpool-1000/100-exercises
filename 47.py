l=[]
for i in range(0,26):
    with open(fr'C:\Users\mbhatnagar\OneDrive - WatchGuard Technologies Inc\Desktop\100-exercises\letters\{chr(97+i)}.txt', 'r') as fd:
        data = fd.read()
        if data in "python":
            l.append(data)
print(l)