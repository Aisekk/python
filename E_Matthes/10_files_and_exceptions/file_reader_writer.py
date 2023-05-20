# 10. Файлы и исключения
# Чтение файла 
print('File reading:')
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())
with open('text_files\pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)

print('Reading by rows:')
filename = 'pi_digits.txt'
with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

# Создание списка строк по содержимому файла
print('Creating rows list by file content:')
with open(filename) as file_object:
	lines = file_object.readlines()
for line in lines:
	print(line.rstrip())

# Работа с содержимым файла
print('Work with file content:')
pi_string = ''
for line in lines:
	pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))
pi_string = ''
for line in lines:
	pi_string += line.strip()
print(pi_string)
print(len(pi_string))

print('String slice:')
print(pi_string[:4] + "...")
print(len(pi_string))

# Запись файла
print('\nFile writing:')
print('Writing in empty file:')
filename = 'programming.txt'
with open(filename, 'w') as file_object:
	file_object.write("I love programming.")
with open(filename, 'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love creating new games.\n")

# Присоединение данных к файлу
print('Appending data to file:')
with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")
