def party_planner(cookie,people):
    leftover = None
    num_each = None
    try:
        num_each = cookie // people
        leftover = cookie % people
    except ZeroDivisionError:
        print('Oops, you entered 0 people will be attending.')
        print('Please enter a good number of people for a party.')
    return(num_each,leftover)

#main code block
lets_party = 'y'
while lets_party == 'y':
    cookie = int(input('How many cookies?'))
    people = int(input('How many people?'))
    cookie_each,leftover = party_planner(cookie,people)

    #if cookies_each is not None
    if cookie_each:
        message = '\nLet\'s party! We\'ll have {} people attending.  \
        Each will eat {} cookies with {} leftover.'
        print(message.format(people,cookie_each,leftover))

    lets_party = input('\nWould you like to party? (y or n)')
