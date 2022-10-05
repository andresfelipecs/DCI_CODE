from stat import FILE_ATTRIBUTE_ARCHIVE


fruit_colors = {
    "apple": "red",
    "berries": "blue"
}

for fruit in fruit_colors:
    print(fruit, fruit_colors[fruit])
    
for items in fruit_colors.items():
    print(items)
    k, v = items
    print(k, v)

for k, v in fruit_colors.items():
    print(k,v)
    
