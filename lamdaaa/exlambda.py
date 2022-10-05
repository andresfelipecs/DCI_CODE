books = [
    {"cost": 10, "name": 'Python 2'},
    {"cost": 1, "name": 'Best tourism sites in Napoli'},
    {"cost": 5, "name": 'Basket Weaving for Pros'},
    {"cost": 8, "name": 'Java for dummies'},
]
# print(sorted(books, key=lambda book: book['cost']))

# readable!
func = lambda book: book['cost']
print(sorted(books, key=func, reverse=True))

#def x(book):
# return book['cost]
# reverse sorts

#sort by name
print(sorted(books, key= lambda book: book['name'], reverse=True))

