import time


def fibonacci(n, memo):
    if memo[n] != -1:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


def fibonacci_series(n, memo):
    for i in range(n + 1):
        fibonacci(i, memo)


n = int(input("Position number: "))

# Initialize the memo array with -1 indicating uncomputed values
memo = [-1] * (n + 1)

start_time = time.time()
result = fibonacci(n, memo)
fibonacci_series(n, memo)
end_time = time.time()

taken_time = end_time - start_time

print(f"The {n}th Fibonacci number is: {result}")
print(f"The Fibonacci series up to the {n}th number is:", end=" ")
for i in range(n + 1):
    print(memo[i], end=" ")
print(f"\nTaken time: {taken_time} seconds")
