from employees import FullTimeEmployee, PartTimeEmployee


def main():
    employees = [
        FullTimeEmployee("Ahmed", 101, 8000),
        PartTimeEmployee("Sara", 102, 80, 50),
        FullTimeEmployee("Khalid", 103, 12000),
    ]

    total_salaries = 0
    for employee in employees:
        employee.display_info()
        salary = employee.calculate_salary()
        print(f"Salary: {salary:g} SAR")
        total_salaries += salary

    print(f"Total Salaries: {total_salaries:g} SAR")


if __name__ == "__main__":
    main()
