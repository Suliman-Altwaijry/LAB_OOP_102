from abc import ABC, abstractmethod
from math import isfinite


def validate_nonnegative(value, field):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field} must be a number.")
    if value < 0 or not isfinite(value):
        raise ValueError(f"{field} must be finite and nonnegative.")
    return value


class Employee(ABC):
    def __init__(self, name, employee_id):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a nonempty string.")
        if (isinstance(employee_id, bool)
                or not isinstance(employee_id, int) or employee_id <= 0):
            raise ValueError("Employee ID must be a positive integer.")
        self.name = name.strip()
        self.__employee_id = employee_id

    def get_employee_id(self):
        return self.__employee_id

    def display_info(self):
        print(f"Employee: {self.name} ID: {self.get_employee_id()}", end=" ")

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)
        self.monthly_salary = monthly_salary

    @property
    def monthly_salary(self):
        return self.__monthly_salary

    @monthly_salary.setter
    def monthly_salary(self, value):
        self.__monthly_salary = validate_nonnegative(value, "Monthly salary")

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hours_worked, hourly_rate):
        super().__init__(name, employee_id)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    @property
    def hours_worked(self):
        return self.__hours_worked

    @hours_worked.setter
    def hours_worked(self, value):
        self.__hours_worked = validate_nonnegative(value, "Hours worked")

    @property
    def hourly_rate(self):
        return self.__hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, value):
        self.__hourly_rate = validate_nonnegative(value, "Hourly rate")

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate
