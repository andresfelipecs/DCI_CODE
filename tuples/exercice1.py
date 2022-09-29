# Exercise
# To get a total, we have a function that looks like this, rewrite (refactor) the function to use a while loop

# def total_list(lst):
#     total = 0
#     for item in lst:
#         total += item
#     return total
# # test case
# print(total_list([1,2,3]))   # answer is 6

def refactor(lst):

    total = 0
    start = 0
    while start < len(lst):
        total += lst[start]
        start += 1
    
    return total

print(refactor([3,3,3]))

# while loop: print the following word: "You are 10kg"
counter = 0
weight = ['10kg', '20kg', '30kg']
while counter < len(weight): # 99% # false !    
    print(weight[counter])
    counter += 1

# exercise: Print “I love red”
counter = 0
colors = ['red', 'green','yellow']
while counter < len(colors[:1]):   
    print(f'I love {colors[counter]}')
    counter += 1
