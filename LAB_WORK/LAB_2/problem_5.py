# 5. Write a function that can print your name 5 times using a loop (For or While).

names = input("Enter your name:")

times = int(input("How many times you want to print:"))

# for loop
print("Printing names using for loop")
for i in range(times):
    print("count ",i+1," : ", names)

# while loop
print("Printing names using while loop")
count = 1
while times>0:
    print("count ",count, " : ",names)
    times -=1
    count +=1
