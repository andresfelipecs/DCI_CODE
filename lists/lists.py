names = ["Victor", "Peter", "Mary", "John", "Badara", "Peer"]

# using an index, replace "Peer" with "Malcom X"
names[5] = "Malcom X"
print(names)

# adds an element at the specified position
names.insert(4, "david")
print(names)

# Add two names to the list of names
add_names = ["alberto", "sofia"]
names.extend(add_names)
print(names)


# Experiment with the methods in a list using dir(names)
#print(dir(names))
#help(dir(names))

names.reverse()
print(names)

names.pop(5)
print(names)
