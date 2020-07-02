def create_dic_flower(filename):
    dic_flower = {}
    with open(filename) as f:
        for line in f:
            letter = line.split(':')[0].lower()
            flower = line.split(':')[1].strip()
            dic_flower[letter] = dic_flower
    return dic_flower

def main():
    dic_flower = create_dic_flower('flower.txt')
    #there is a text file
    name = input('Enter your First[space]Lastname only:')
    first_name = name[0].lower()
    letter = first_name[0]
    print('Unique flower: {}'.format(dic_flower[letter]))

if __name__=='__main__':
    main()
