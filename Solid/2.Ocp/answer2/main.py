from employee import Employee, EmployeeType

if __name__ == "__main__":
    full_time_employee = Employee("Alice", EmployeeType.FullTime)
    print(
        f"{full_time_employee.name}'s salary is {full_time_employee.calulate_salary()}"
    )

    intern_employee = Employee("Bob", EmployeeType.Intern)
    print(f"{intern_employee.name}'s salary is {intern_employee.calulate_salary()}")
