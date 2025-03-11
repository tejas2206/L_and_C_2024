class Employee:
    def __init__(self, name: str, age: int, salary: float):
        self._name = name
        self._age = age
        self._salary = salary

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str):
        self._name = name

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int):
        self._age = age

    def get_salary(self) -> float:
        return self._salary

    def set_salary(self, salary: float):
        self._salary = salary


employee = Employee('Tejas', 22, 23.45)

#Is employee an object or a data structure? Why?

#It behaves more like a data structure because it only stores data with simple getters and setters without any real behavior. 
#A better object-oriented approach would include methods that operate on the data."""
