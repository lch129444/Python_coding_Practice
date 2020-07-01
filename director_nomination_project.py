nominated = {1931:['Norman Tib','Wesley Roth'],1932:['Frank B','Wesley Roth'],1933:['Norman Tib','Jack Lee'],1934:['Frank B','Andrew Young']}
winners = {1931:['Norman Tib'],1932:['Frank B'],1933:['Jack Lee'],1934:['Frank B']}
#count each director's num of being nominated, count win times
nom_count_dict = {}
print("Nomination count:")
for year, list_dirc in nominated.items():
    for director in list_dirc:
        if director not in nom_count_dict:
            nom_count_dict[director] = 1
        else:
            nom_count_dict[director] += 1
print('nom_count_dict = {}\n'.format(nom_count_dict))

#count each winner's winning times
print('Winning count:')
win_count_dict = {}
for year, winner_list in winners.items():
    for winner in winner_list:
        win_count_dict[winner] = win_count_dict.get(winner,0)+1
print('win_count_dict = {}\n'.format(win_count_dict))

#find the director who win most times and the highest winning times:
print('The director who won most times and the highest winning times:')
print('Method 1')
highest_count = 0
most_win_director = []
for key, value in win_count_dict.items():
    if value > highest_count:
        highest_count = value
        most_win_director.clear()
        #to delete the loser
        most_win_director.append(key)
    elif value == highest_count:
        most_win_director.append(key)
        #if not this one, tie directors will be omitted
    else:
        continue
print('most_win_director is{}'.format(most_win_director))
print('highest_winning_count is {}'.format(highest_count))


print('\nMethod 2')
highest_count = max(win_count_dict.values())
#easier way
most_win_director = [key for key, value in win_count_dict.items() if value == highest_count]
print('most_win_director is{}'.format(most_win_director))
print('highest_winning_count is {}'.format(highest_count))
