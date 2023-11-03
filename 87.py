miss = ['Portugal', 'Germany', 'Spain']
with open('countries_missing.txt', 'a') as f:
    f.writelines([f'{m}\n' for m in miss])