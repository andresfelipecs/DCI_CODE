name = ('Mirjam', 'Lingoda')
other_name = ('Peer', 'Hofman')

# tuples (are immutable)

name = name + other_name
print(name)

numbers = (1,2,3,4,5,6,7,8,9)
print(numbers[0:1]) # 2, 3, 4, 5

# inbuilt "len" function/method
print(len(numbers))
print(numbers[0])

# negative indexing
print(numbers[-2])
print(numbers[-9])

#tuple type
print(type(numbers))