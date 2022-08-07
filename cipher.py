def run():
    secret = 'communication_is_a_key_factor'
    name = 'felipe'
    year = '1995'
    
    one = secret + name
    two = one[::-1]
    next = two + year
    print(next)


if __name__ == '__main__':
    run()