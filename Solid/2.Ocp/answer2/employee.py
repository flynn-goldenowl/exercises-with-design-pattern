from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def calculate_salary(self) -> int:
        raise NotImplementedError


class FullTime(Employee):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def calculate_salary(self) -> int:
        return 5000


class PartTime(Employee):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def calculate_salary(self) -> int:
        return 3000

class Intern(Employee):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def calculate_salary(self) -> int:
        return 1000

class Freelancer(Employee):
    def __init__(self, name: str, working_time: int) -> None:
        super().__init__(name)
        self.working_time = working_time

    def calculate_salary(self) -> int:
        return 40 * self.working_time
