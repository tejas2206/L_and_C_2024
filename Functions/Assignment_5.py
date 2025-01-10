class Employee:
    def __init__(self, employee_id, name, department, is_active):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.is_active = is_active

    def terminate(self):
        self.is_active = False

    def is_active_employee(self):
        return self.is_active


class EmployeeRepository:
    @staticmethod
    def save(employee):
        print(f"Saving {employee.name} to the database.")


class EmployeeReport:
    @staticmethod
    def generate_xml_report(employee):
        return (
            f"<employee>"
            f"<employee_id>{employee.employee_id}</employee_id>"
            f"<name>{employee.name}</name>"
            f"<department>{employee.department}</department>"
            f"</employee>"
        )

    @staticmethod
    def generate_csv_report(employee):
        return f"{employee.employee_id},{employee.name},{employee.department}"


if __name__ == "__main__":
    employee = Employee(1, "Tejas", "DE", True)
    EmployeeRepository.save(employee)
    print(EmployeeReport.generate_xml_report(employee))
    print(EmployeeReport.generate_csv_report(employee))
