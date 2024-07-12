import time

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)
    
# Get the number from the user
n = int(input("Enter the position of the Fibonacci number you want: "))

# Measure the time taken to compute the Fibonacci number
start_time = time.time()
result = fib(n)
end_time = time.time()


# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the Fibonacci number and the elapsed time
print(f"The {n}th Fibonacci number is: {result}")
print(f"Time taken to compute: {elapsed_time} seconds")
