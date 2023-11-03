from collections import OrderedDict
# Question: Complete the script so that it removes duplicate items from the list a .

a = ["1", 1, "1", 2]
print(list(set(a)))

# Preserving the order
a = list(OrderedDict.fromkeys(a))
print(a)