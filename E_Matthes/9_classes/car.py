"""Класс для представления автомобиля."""
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
		"""У бензомобилей есть бензобак."""
		print("This car does need a gas tank!")


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


