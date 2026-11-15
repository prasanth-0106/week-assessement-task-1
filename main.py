from functools import wraps
import csv

def calculate_bonus(salary, rate=0.1, *extras, **options):
    bonus = salary * rate + sum(extras)
    if "cap" in options:
        bonus = min(bonus, options["cap"])
    return bonus

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"{self.name} - {self.salary}"

    @property
    def annual_salary(self):
        return self.salary * 12

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    @log_call
    def get_details(self):
        return f"{self.name} - {self.salary} - Team Size: {self.team_size}"

def main():
    with open("employees.csv", newline="", encoding="utf-8") as file:
        for employee in csv.DictReader(file):
            salary = int(employee["salary"])
            if salary < 50000:
                category = "Low"
            elif salary < 70000:
                category = "Medium"
            else:
                category = "High"
            print(f"{employee['name']} - {category} Salary")

    manager = Manager("Divya", 75000, 5)
    print(manager.get_details())

if __name__ == "__main__":
    main()
