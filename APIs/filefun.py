import requests
import pprint
# f = open('book.txt')
# # read the contents of the file
# lines = f.readlines()
# print(lines)

# Writing to a file
# f = open('book.txt', 'a') # append to a file
# # write
# f.write("Hello class")
# # close the file descriptor 
# f.close()
    
# f = open('book.txt', 'a')
# for i in range(1000):
#     #print(i)
#     f.write(f'{i}\n')
# f.close()

r = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
#print(r.json())
pprint.pprint(r.json())