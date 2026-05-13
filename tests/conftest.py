import pytest
from calculator import Car, ElectricCar, Calculator


@pytest.fixture(scope="session")
def car():
    print("\nCreating a new car\n")
    return Car("Toyota Corolla", price=30000,
               fuel_economy=7, service_cost=1200, insurance_cost=2500)


@pytest.fixture
def electric_car():
    return ElectricCar("Tesla", 10000, 5000, 150)


@pytest.fixture
def calculator(car):
    res = Calculator()
    res.add_car(car)
    return res
