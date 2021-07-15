demo_list = [1, 'hello', 1.34, True, [1, 2, 3]]
colors = ['red', 'green', 'blue']

numbers_list = list((1, 2, 3, 4))
print(numbers_list)

r = list(range(1, 100))
print(r)
print(len(colors))
print(colors[1])
print('green' in colors)
print(colors)
colors[1] = 'yellow'
print(colors)

colors.append('violet')
colors.extend(['violet', 'yellow'])
colors.extend('pink', 'black')
colors.insert(len(colors),'violet')

print(colors)

colors.pop()
print(colors)

print(colors)

colors.clear()
print(colors)

colors.sort()
print(colors)

print(colors)
print(colors)

print(colors.index('red'))
print(colors.count('red'))
