names = ['jacque doe', 'peer doe', 'mirjam doe', 'shaban doe']

print(list(map(lambda name: name.title(), names)))


names2 = ['reiner', 'peter', 'john']

finish_er = list(filter(lambda x: x.endswith('er') == False, names2))
print(finish_er)

names3 = [{'name': 'jacque doe'}, {'name': 'peer doe'}, {'name': 'mirjam doe'}, {'name': 'shaban doe'}]

remove = list(filter(lambda x : x['name'] != 'jacque doe',names3))
print(remove)