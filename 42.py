# Question: Print out in each line the sum of homologous items of the two sequences.

a = [1, 2, 3]
b = (4, 5, 6)

for num1, num2 in zip(a, b):
    print(num1 + num2)