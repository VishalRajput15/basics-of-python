#nested list and flatten 

nested_list = [['Rohit Sharma','Jasprit Bumrah','Suryakumar Yadav'], ['Virat Kohli','AB Devillers'], ['MSD','Suresh Raina','Mathew Hyden']]

flattened = [item for sublist in nested_list for item in sublist]

print(flattened)
