# 10. Исключения
print('Exceptions')
try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")

# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
# while True:
	# first_number = input("\nFirst number: ")
	# if first_number == 'q':
		# break
	# second_number = input("Second number: ")
	# try:
		# answer = int(first_number) / int(second_number)
	# except ZeroDivisionError:
		# print("You can't divide by 0!")
	# else:
		# print(answer)

filename = 'alice.txt'
try:
	with open(filename) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = "Sorry, the file " + filename + " does not exist."
	print(msg)
else:
	# Подсчет приблизительного количества слов в файле.
	words = contents.split()
	num_words = len(words)
	print("The file " + filename + " has about " + str(num_words) + " words.")

# JSON module
print('JSON module:')
import json
# Программа загружает имя пользователя, если оно было сохранено ранее.
# В противном случае она запрашивает имя пользователя и сохраняет его.

def get_stored_username():
	"""Получает хранимое имя пользователя, если оно существует."""
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username
		
def get_new_username():
	"""Запрашивает новое имя пользователя."""
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
		return username

def greet_user():
	"""Приветствует пользователя по имени."""
	username = get_stored_username()
	if username:
		print("Welcome back, " + username + "!")
	else:
		username = get_new_username()
		print("We'll remember you when you come back, " + username + "!")

greet_user()
