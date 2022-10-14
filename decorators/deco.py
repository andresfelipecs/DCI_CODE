# def outer(name):
#     def inner():
#         print(f'Hello {name}, I am inner')
#         return 'Return value'
#     return inner

# outer('Felipe')()

# c = outer('Felipe')
#Hello Felipe, I am inner

# print(c())
#Hello Felipe, I am inner
#Return value

# def make_title(func): # we expect the function to return a string
#     def inner(suffix):
#         return func(suffix).title()
#     return inner        

# @make_title
# def greetings(suffix):
#     return "mr. {0}".format(suffix)

# print(greetings('fausto doe'))

def add_mr(function):
    def inner(*args):
    #     full_string = ''
    #     for s in args: 
    #         full_string += s + ' '
        name = f"Mr/Mrs {' '.join([ n.title() for n in args])}"
        return function(name)
    return inner        

@add_mr
def greet_some_humans(name):
    # API, Test driven development
    return "Good morning " + name    

print(greet_some_humans('peer', 'doe', 'johnson', 'MP', 'Felipe'))