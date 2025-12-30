# Dictionary sort by values

fruits = {'Apple': 10, 'Banana': 5, 'Chikoo': 20}
sortedDict = dict(sorted(fruits.items(), key=lambda item: item[1]))
print(sortedDict)