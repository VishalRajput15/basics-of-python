#remove duplicates from list

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

items = [1, 2, 2, 3, 4, 4, 5, "Apple", "Apple"]
cleanList = remove_duplicates(items)
print(cleanList)