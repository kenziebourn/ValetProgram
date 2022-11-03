
import unittest
from ValetSimulator import Car
from ValetSimulator import Garage
from ValetSimulator import LotFullError
from ValetSimulator import Motorcycle
from ValetSimulator import UnavailableError

class TestVehicle(unittest.TestCase):
    def test_1(self):
        "checks whether LotFullError is raised when there are no more remaining spots in the garage"
        with self.assertRaises(LotFullError):
            my_lot = Garage()
            my_lot.add_vehicle(Car('130', 'McKenzie', 'Silver', 'Mercedes-AMG', 'GT'))
            my_lot.add_vehicle(Car('131', 'Thalia', 'Black', 'Porsche', 'Macan'))
            my_lot.add_vehicle(Car('132', 'Tom', 'White', 'Jeep', 'Renegade'))
            my_lot.add_vehicle(Motorcycle('133', 'Mohommad', 'Green', 'Kawasaki', 'Ninja H2R'))
            my_lot.add_vehicle(Car('134', 'Promish', 'Black', 'BMW', '330i'))
            my_lot.add_vehicle(Car('135', 'Celeste', 'Red', 'Lamborghini', 'Aventador'))
            my_lot.add_vehicle(Car('136', 'Dave', 'Gray', 'Nissan', 'Altima'))
            my_lot.add_vehicle(Car('137', 'Angelo', 'Orange', 'Kia', 'Soul'))
            my_lot.add_vehicle(Motorcycle('138', 'Aiden', 'Yellow', 'BMW', 'S1000RR'))
            my_lot.add_vehicle(Car('139', 'Mishka', 'Purple', 'Lamborghini', 'Huracan'))
            my_lot.add_vehicle(Car('140', 'Sam', 'White', 'Jeep', 'Wrangler'))
            my_lot.add_vehicle(Car('141', 'Andellyn', 'Gray', 'Nissan', 'Sentra'))
            my_lot.add_vehicle(Car('142', 'Ajesh', 'Silver', 'Mazda', 'CX-5'))
            my_lot.add_vehicle(Car('143', 'Aryan', 'Red', 'Honda', 'CRV'))
            my_lot.add_vehicle(Car('144', 'Tim', 'Black', 'Hyundai', 'Elantra'))
            my_lot.add_vehicle(Motorcycle('145', 'Chris', 'Red', 'Honda', 'CBR'))
            my_lot.add_vehicle(Car('146', 'Stefan', 'Silver', 'Mercedes-AMG', 'GT'))
            my_lot.add_vehicle(Car('147', 'Damon', 'Black', 'Porsche', 'Macan'))
            my_lot.add_vehicle(Car('148', 'Kai', 'White', 'Jeep', 'Renegade'))
            my_lot.add_vehicle(Motorcycle('149', 'Klaus', 'Green', 'Kawasaki', 'Ninja H2R'))
            my_lot.add_vehicle(Car('150', 'Elijah', 'Black', 'BMW', '330i'))
            my_lot.add_vehicle(Car('151', 'Elena', 'Red', 'Lamborghini', 'Aventador'))
            my_lot.add_vehicle(Car('152', 'Yash', 'Gray', 'Nissan', 'Altima'))
            my_lot.add_vehicle(Car('153', 'Hrithik', 'Orange', 'Kia', 'Soul'))
            my_lot.add_vehicle(Motorcycle('154', 'Arjit', 'Yellow', 'BMW', 'S1000RR'))
            my_lot.add_vehicle(Car('155', 'Alia', 'Purple', 'Lamborghini', 'Huracan'))
            my_lot.add_vehicle(Car('156', 'Tokyo', 'White', 'Jeep', 'Wrangler'))
            my_lot.add_vehicle(Car('157', 'Dean', 'Blue', 'Nissan', 'Sentra'))
            my_lot.add_vehicle(Car('158', 'Theo', 'Silver', 'Mazda', 'CX-5'))
            my_lot.add_vehicle(Car('159', 'Christian', 'Red', 'Honda', 'CRV'))
            my_lot.add_vehicle(Car('160', 'Jia', 'Black', 'Hyundai', 'Elantra'))

    def test_2(self):
        """checks whether UnavailableError is raised when a non-existent ticket number is entered into database"""
        with self.assertRaises(UnavailableError):
            my_lot = Garage()
            my_lot.add_vehicle(Car('130', 'McKenzie', 'Silver', 'Mercedes-AMG', 'GT'))
            my_lot.add_vehicle(Car('131', 'Thalia', 'Black', 'Porsche', 'Macan'))
            my_lot.add_vehicle(Car('132', 'Tom', 'White', 'Jeep', 'Renegade'))
            my_lot.remove_vehicle('170', '10')

    #def test_3(self):


    #def test_4(self):


    #def test_5(self):

if __name__ == '__main__':
    unittest.main()