class Employee:
    def __init__(self, emp_id, name, department, working):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.working = working

    def terminate_employee(self):
        self.working = False

    def is_working(self):
        return self.working


class EmployeeRepository:
    @staticmethod
    def save_to_database(employee):
        print(f"Saving {employee.name} to database.")


class EmployeeReport:
    @staticmethod
    def generate_report_xml(employee):
        return f"<employee><id>{employee.emp_id}</id><name>{employee.name}</name><department>{employee.department}</department></employee>"

    @staticmethod
    def generate_report_csv(employee):
        return f"{employee.emp_id},{employee.name},{employee.department}"

emp = Employee(1, "John Doe", "IT", True)
EmployeeRepository.save_to_database(emp)
print(EmployeeReport.generate_report_xml(emp))
print(EmployeeReport.generate_report_csv(emp))