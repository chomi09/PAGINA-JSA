demo_list = [1,'hello', 1.32, True, [1,2,3,4]]
number_list = list((1, 2, 3, 4))
colors = ['red', 'orange', 'blue']
#print(number_list)

#r = list(range(1, 100))
#print(r)
print(len(colors))
print(colors[2])
print('blue' in colors)
print('green' in colors)

print(colors)
#colors[1] = 'green'
print(colors)

print('--------------------------------------')
#colors.append (['violet', 'yellow'])
#colors.extend(('violet', 'yellow'))
print(colors)
colors.insert(1, 'violet')
print(colors)
colors.insert(len(colors), 'hellow')
print(colors)
#colors.pop()
#colors.pop()
print(colors)
colors.remove ('blue')
print(colors)
colors.pop(2)
print(colors)
#colors.clear
print(colors)

print('----------------------------------------')
color = ['red', 'orange', 'blue']
#color.sort()
#color.sort(reverse=True)
print(color.index('red'))
print(color.count('red'))