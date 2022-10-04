

from audioop import reverse


lists = [ ["John",[ {"name": "Mary"} ], "Amy"], [ 32, 43,{'age': 100}, 51] ]

print(lists[0][1][0]['name'])
print(lists[1][2]['age'])

dic = {'hole':'hello', 'ggg':'hhh'}

for k,v in dic.items():
    print(k, v)

for k in dic.keys():
    print(k)

for v in dic.values():
    print(v)

words = ['cat', 'aadvark', 'elephant', 'squirrel', 'hippo']
words.sort()
print(words)
words.sort(reverse=True)
print(words)