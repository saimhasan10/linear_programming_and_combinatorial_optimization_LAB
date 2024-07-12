import time


def fibonacci(n):
    if n <= 1:
        return n

    # Initialize the memoization array
    memo = [0] * (n + 1)
    memo[0] = 0
    memo[1] = 1

    
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n], memo


n = int(input("Position number: "))

start_time = time.time()
result, series = fibonacci(n)
end_time = time.time()

taken_time = end_time - start_time

print(f"The {n}th Fibonacci number is: {result}")
print(f"The Fibonacci series up to the {n}th number is:", end=" ")
for num in series:
    print(num, end=" ")
print(f"\nTaken time: {taken_time} seconds")
