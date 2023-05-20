# if command
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

car = 'bmw'
print(car == 'bmw')
car = 'audi'
print(car == 'bmw')
car = 'Audi'
print(car == 'audi')
print(car.lower() == 'audi')

print('\nnums:')
age_0 = 19
age_1 = 21
print(age_0 > 18 and age_1 >= 21)
print(age_0 > 21 and age_1 >= 21)
print(age_0 > 21 or age_1 >= 21)

print('requested_toppings')
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

print('\nbanned_users')
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
	print(user.title() + ", you can post a response if you wish.")

age = 17
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")

age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 5
else:
	price = 10
print("Your admission cost is $" + str(price) + ".")
	
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		print("Adding " + requested_topping + ".")
print("Finished making your pizza!")

requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + ".")
		print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")

# dictionaries 
print('---------------------------------------------')
print('dictionaries:')
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print('del alien points:')
del alien_0['points']
print(alien_0)

print('iterating k,v:')
user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
}
for key, value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value)

print('\nfavorite_languages:')	
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}
for name in favorite_languages.keys():
	print(name.title())
	
print('sorted iterating:')
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")

print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())

print('Remove duplicates by set():')
for language in set(favorite_languages.values()):
	print(language.title())

print('Nested dict-s:')	
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
	print(alien)

print('\n30 aliens:')
# Создание пустого списка для хранения пришельцев.
aliens = []
# Создание 30 зеленых пришельцев.
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)
# Вывод первых 5 пришельцев:
for alien in aliens[:5]:
	print(alien)
print("...")
# Вывод количества созданных пришельцев.
print("Total number of aliens: " + str(len(aliens)))

print('List in dict:')
# Сохранение информации о заказанной пицце.
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
}
# Описание заказа.
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")
for topping in pizza['toppings']:
	print("\t" + topping)

favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are:")
	for language in languages:
		print("\t" + language.title())

print('Dict. in dict.:')		
users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
},
}
for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())
	
