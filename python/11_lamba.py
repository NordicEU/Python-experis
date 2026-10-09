def get_salary(employee):
    return employee["salary"]

employees = [
    {"name": "Alice", "salary": 50000},
    {"name": "Bob", "salary": 60000},
    {"name": "Charlie", "salary": 40000}
]
sorted_employees = sorted(employees, key=get_salary, reverse=True)

sorted_employees = sorted(employees, key=lambda employee: employee["salary"], reverse=True)

print(sorted_employees)