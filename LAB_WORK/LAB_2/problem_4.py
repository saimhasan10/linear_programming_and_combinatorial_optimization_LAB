"""
4. cars = ["Ford","Volvo","BMW"] In this list add Honda,
delete Volvo using function,
and delete Ford using value.
"""
def delete_car(lst, car):
    if car in lst:
        lst.remove(car)
        print(f"After deleting {car}:", lst)
    else:
        print(f"{car} is not in the list.")


cars = ["Ford", "Volvo", "BMW"]

# adding honda
cars.append("Honda")
cars.insert(2,"Mustang") # adding in index wise
cars.extend(["Mercedes", "Nissan"])  # Adds elements from another list to the end
print("After adding the list is:", cars)


#  deleting

# Deleting Volvo using function
delete_car(cars, "Volvo")
cars.remove("Ford")
print("After deleting Ford", cars)
