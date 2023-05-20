# 8. functions
import pizza
import pizza as p
from pizza import foo
from pizza import foo as alias_foo
from my_module import *

def greet_user(username):
	"""Выводит простое приветствие."""
	print("Hello, " + username.title() + "!")
greet_user('jesse')

print('pets:')
def describe_pet(animal_type, pet_name):
	"""Выводит информацию о животном."""
	print("I have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')

print('\nNamed args:')
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

print('\nReturn simple value:')
def get_formatted_name(first_name, last_name, middle_name=''):
	"""Возвращает аккуратно отформатированное полное имя."""
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

print('\nDict. return:')
def build_person(first_name, last_name, age=''):
	"""Возвращает словарь с информацией о человеке."""
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

print('\nPass list in func:')
def greet_users(names):
	"""Вывод простого приветствия для каждого пользователя в списке."""
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

print('\nChange list in func:')
# Список моделей, которые необходимо напечатать.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Цикл последовательно печатает каждую модель до конца списка.
# После печати каждая модель перемещается в список completed_models.
while unprinted_designs:
	current_design = unprinted_designs.pop()
	# Печать модели на 3D-принтере.
	print("Printing model: " + current_design)
	completed_models.append(current_design)

# Вывод всех готовых моделей.
print("The following models have been printed:")
for completed_model in completed_models:
	print(completed_model)

print('\nPartition on 2 func:')
def print_models(unprinted_designs, completed_models):
	"""
	Имитирует печать моделей, пока список не станет пустым.
	Каждая модель после печати перемещается в completed_models.
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		# Имитация печати модели на 3D-принтере.
		print("Printing model: " + current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
	"""Выводит информацию обо всех напечатанных моделях."""
	print("The following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Запрет изменения списка в функции
print('\nPass list copy in func:')
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)
print('init list saved: ' + str(unprinted_designs))

# Передача произвольного набора аргументов
print('\nPassing an arbitrary set of arguments:')
def make_pizza(*toppings):
	"""Вывод списка заказанных дополнений."""
	print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(*toppings):
	"""Выводит описание пиццы."""
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Позиционные аргументы с произвольными наборами аргументов
print('Positional arguments with arbitrary argument sets: ')
def make_pizza(size, *toppings):
	"""Выводит описание пиццы."""
	print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Использование произвольного набора именованных аргументов
print('Using an arbitrary set of named arguments: ')
def build_profile(first, last, **user_info):
	"""Строит словарь с информацией о пользователе."""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

print('\nimport pizza: ')
p.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print('\nfrom pizza import foo: ')
foo(568)
alias_foo(299)

print('\nfrom my_module import *: ')
foo_num(100)
foo_str(200)
