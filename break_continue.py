manifest = [('banana',15),['mattress',24],('cheese',5),('apple',20),('table',50),('watermalon',20),('orange',15)]
print('Method 1')
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print('current weight:{}'.format(weight))
    if weight >= 100:
        print('break the loop now!')
        break
    else:
        print('adding {}({})'.format(cargo_name,cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight
print('\n Final Weight:{}'.format(weight))
print('Final Items:{}'.format(items))

print('Method 2')
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print('current weight:{}'.format(weight))
    if weight >= 100:
        print('break the loop now!')
        break
    elif weight + cargo_weight > 100:
        print('skipping{}({})'.format(cargo_name,cargo_weight))
        continue
    else:
        print('adding {}({})'.format(cargo_name,cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight
print('\n Final Weight:{}'.format(weight))
print('Final Items:{}'.format(items))
