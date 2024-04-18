# Create 5 different variables and list them in python then print the variables and their types.


name = "Minions"
id = 999
salary = 12000.00
is_employee = True
car_collections = ("Dodge", "Mustang")

list = [name, id, salary, is_employee, car_collections]

for var in list:
    print("variable name: ", var, "the type is:", type(var))
