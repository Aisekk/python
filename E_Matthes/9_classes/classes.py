# 9. classes
print('Python classes.')

class Dog():
	"""Простая модель собаки."""
	def __init__(self, name, age):
		"""Инициализирует атрибуты name и age."""
		self.name = name
		self.age = age
	
	def sit(self):
		"""Собака садится по команде."""
		print(self.name.title() + " is now sitting.")
		
	def roll_over(self):
		"""Собака перекатывается по команде."""
		print(self.name.title() + " rolled over!")

my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

class Car():
	"""Простая модель автомобиля."""
	def __init__(self, make, model, year):
		"""Инициализирует атрибуты описания автомобиля."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	
	def get_descriptive_name(self):
		"""Возвращает аккуратно отформатированное описание."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		"""Выводит пробег машины в милях."""
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self, mileage):
		"""
		Устанавливает на одометре заданное значение.
		При попытке обратной подкрутки изменение отклоняется.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
	
	def increment_odometer(self, miles):
		"""Увеличивает показания одометра с заданным приращением."""
		self.odometer_reading += miles
	
	def fill_gas_tank():
		pass

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
my_new_car.update_odometer(46)
my_new_car.read_odometer()
my_new_car.increment_odometer(4)
my_new_car.read_odometer()

class Battery():
	"""Простая модель аккумулятора электромобиля."""
	def __init__(self, battery_size=85):
		"""Инициализирует атрибуты аккумулятора."""
		self.battery_size = battery_size
	
	def describe_battery(self):
		"""Выводит информацию о мощности аккумулятора."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")
	
	def get_range(self):
		"""Выводит приблизительный запас хода для аккумулятора."""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
			
			message = "This car can go approximately " + str(range)
			message += " miles on a full charge."
			print(message)
	
class ElectricCar(Car):
	"""Представляет аспекты машины, специфические для электромобилей."""
	def __init__(self, make, model, year):
		"""
		Инициализирует атрибуты класса-родителя.
		Затем инициализирует атрибуты, специфические для электромобиля.
		"""
		super().__init__(make, model, year)
		self.battery_size = 70
		self.battery = Battery()

	def describe_battery(self):
		"""Выводит информацию о мощности аккумулятора."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")
		
	def fill_gas_tank():
		"""У электромобилей нет бензобака."""
		print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# Стандартная библиотека Python
print('\nStandard Python Library:')
from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + language.title() + ".")

