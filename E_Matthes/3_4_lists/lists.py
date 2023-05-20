print('3.Lists:')
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
print('')

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

print('append():')
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

print('insert():')
motorcycles.insert(0, 'ducati')
print(motorcycles)

print('del')
del motorcycles[0]
print(motorcycles)

print('pop():')
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

print('pop(i):')
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

print('remove(value):')
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("A " + too_expensive.title() + " is too expensive for me.")

print('sort():')
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)

print('sort(reverse=True):')
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

print('sorted():')
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

print('reverse():')
cars.reverse()
print(cars)

print('len():')
len(cars)

print('\n4.Lists work:')
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)

print('\nnums:')
for value in range(1,5):
	print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

print('squares:')
squares = []
for value in range(1,11):
	#square = value**2
	squares.append(value**2)
print(squares)

print('digits:')
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

print('lists generators:')
squares = [value**2 for value in range(1,11)]
print(squares)

print('slices:')
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
print("Here are the first three players on my team:")

print('for in slices:')
for player in players[:3]:
	print(player.title())

print('\nlists copying:')
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)

print('\nreference to list:')
my_foods = ['pizza', 'falafel', 'carrot cake']
# This doesn't work:
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

print('\ntuples:')
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
#dimensions[0] = 250

for dimension in dimensions:
	print(dimension)

print('\ntuple assign:')
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)
