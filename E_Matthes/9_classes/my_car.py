#from car import Car
#from car import ElectricCar
#from car import Car, ElectricCar
import car
#from имя_модуля import * # not recommend

# my_new_car = Car('audi', 'a4', 2016)
my_new_car = car.Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla = car.ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()



