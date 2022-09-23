

def full_names(*args): # define function using *args
    # input as any args as we want :D
    
    full_name = '' # define variable with empty string
    # () tuple {} dictionary [] list 
    for arg in args: # for loop iteration
        full_name += f'{arg} ' # concatenating arg to variable full_name
    
    print(full_name) #printing

full_names('A', 'B', 'C') # calling function
#full_names('A', 'B')
#full_names('A')