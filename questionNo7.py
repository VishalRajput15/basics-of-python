#generator for even numbers 

def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

for num in even_numbers(10):
    print(num, end=" ")