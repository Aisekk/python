# input() and while()
# name = input("Please enter your name: ")
# print("Hello, " + name + "!")

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# active = True
# while active:
	# message = input(prompt)
	# if message == 'quit':
		# active = False
	# else:
		# print(message)

# break
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "
# while True:
	# city = input(prompt)
	# if city == 'quit':
		# break
	# else:
		# print("I'd love to go to " + city.title() + "!")

# continue
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
	print(current_number)

# Начинаем с двух списков: пользователей для проверки
# и пустого списка для хранения проверенных пользователей.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Проверяем каждого пользователя, пока остаются непроверенные
# пользователи. Каждый пользователь, прошедший проверку,
# перемещается в список проверенных.
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)
# Вывод всех проверенных пользователей.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())
	
# Удаление всех вхождений конкретного значения из списка
print('\nRemove all matches:')
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
	pets.remove('cat')
print(pets)

# Заполнение словаря данными, введенными пользователем
print('Filling the dictionary with data entered by the user:')
responses = {}
# Установка флага продолжения опроса.
polling_active = True
while polling_active:
	# Запрос имени и ответа пользователя.
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb someday? ")
	# Ответ сохраняется в словаре:
	responses[name] = response
	# Проверка продолжения опроса.
	repeat = input("Would you like to let another person respond? (yes/ no) ")
	if repeat == 'no':
		polling_active = False

# Опрос завершен, вывести результаты.
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(name + " would like to climb " + response + ".")

