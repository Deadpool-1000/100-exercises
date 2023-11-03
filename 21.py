# Question: Filter the dictionary by removing all items with a value of greater than 1.

d = {"a": 1, "b": 2, "c": 3}

d = {key:item for key,item in d.items() if item<=1}
print(d)
