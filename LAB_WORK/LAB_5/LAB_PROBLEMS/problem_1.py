import time


def fibonacci(n):
    if n == 0:
        return [0], 0
    elif n == 1:
        return [0, 1], 1

    series = [0, 1]
    for i in range(2, n + 1):
        series.append(series[-1] + series[-2])

    return series, series[-1]

n = int(input("Position number: "))

start_time = time.time()
series, result = fibonacci(n)
end_time = time.time()


taken_time = end_time - start_time

print(f"The {n}th fibonacci number is: {result}")
print(f"The Fibonacci series up to the {n}th number is:", end=" ")
for number in series:
    print(number, end=" ")
print(f"\nTaken time {taken_time} seconds")
