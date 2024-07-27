#!/usr/bin/env python3

# Add the project root directory to the Python path
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)
from lib.car import Car
from lib.vehicle import Vehicle

# from car import Car
# from vehicle import Vehicle

class TestVehicle:
    '''Class "Vehicle" in vehicle.py'''

    def test_is_class(self):
        '''is really a class.'''
        assert(object in Vehicle.__bases__)

    def test_has_wheel_size(self):
        '''instantiates with attribute "wheel_size".'''
        my_vehicle = Vehicle(48, 4)
        assert(my_vehicle.wheel_size == 48)

    def test_has_wheel_number(self):
        '''instantiates with attribute "wheel_number".'''
        my_vehicle = Vehicle(48, 4)
        assert(my_vehicle.wheel_number == 4)

    def test_goes_vroom(self):
        '''has a method "go()" that goes "vrrrrrrrooom!"'''
        my_vehicle = Vehicle(48, 4)
        assert(my_vehicle.go() == "vrrrrrrrooom!")

    def test_fills_tank(self):
        '''has a method "fill_up_tank" that returns "filling up!"'''
        my_vehicle = Vehicle(48, 4)
        assert(my_vehicle.fill_up_tank() == "filling up!")

class TestCar:
    '''Class "Car" in car.py'''

    def test_is_subclass(self):
        '''is really a subclass of Vehicle.'''
        assert(Vehicle in Car.__bases__)

    def test_has_wheel_size(self):
        '''instantiates with attribute "wheel_size".'''
        my_car = Car(36, 4)
        assert(my_car.wheel_size == 36)

    def test_has_wheel_number(self):
        '''instantiates with attribute "wheel_number".'''
        my_car = Car(36, 4)
        assert(my_car.wheel_number == 4)

    def test_goes_vroom(self):
        '''has a method "go()" that goes "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"'''
        my_car = Car(48, 4)
        assert(my_car.go() == "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!")

    def test_fills_tank(self):
        '''has a method "fill_up_tank" that returns "filling up!"'''
        my_car = Car(36, 4)
        assert(my_car.fill_up_tank() == "filling up!")