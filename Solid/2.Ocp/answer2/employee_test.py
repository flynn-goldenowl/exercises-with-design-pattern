import unittest
from employee import FullTime, PartTime, Intern, Freelancer


class TestEmployee(unittest.TestCase):
    def test_full_time_salary(self):
        employee = FullTime(name="Alice")
        self.assertEqual(employee.calculate_salary(), 5000)

    def test_part_time_salary(self):
        employee = PartTime(name="Bob")
        self.assertEqual(employee.calculate_salary(), 3000)

    def test_intern_salary(self):
        employee = Intern(name="Charlie")
        self.assertEqual(employee.calculate_salary(), 1000)

    def test_freelancer_salary(self):
        employee = Freelancer(name="Dave", working_time=100)
        self.assertEqual(employee.calculate_salary(), 40 * 100)


if __name__ == "__main__":
    unittest.main()
