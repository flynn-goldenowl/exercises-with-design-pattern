from enum import Enum, auto


class EmployeeType(Enum):
    FullTime = auto()
    PartTime = auto()
    Intern = auto()


EmployeeSalary = {
    EmployeeType.FullTime: 5000,
    EmployeeType.PartTime: 3000,
    EmployeeType.Intern: 1000,
}


class Employee:
    def __init__(self, name: str, type: EmployeeType) -> None:
        self.name = name
        self.type = type

    def calulate_salary(self) -> int:
        try:
            return EmployeeSalary[self.type]
        except KeyError:
            print("Unknown employee type")
