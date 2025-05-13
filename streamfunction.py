from functools import reduce

def demonstrate_stream_operations():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print("\nStream Operations:")

    squared_numbers = list(map(lambda x: x * x, numbers))
    print(f"Squared numbers: {squared_numbers}")

    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers: {even_numbers}")

    sum_numbers = reduce(lambda x, y: x + y, numbers)
    print(f"Sum of numbers: {sum_numbers}")

    even_squared_sum = reduce(lambda x, y: x + y, map(lambda x: x * x, filter(lambda x: x % 2 == 0, numbers)))
    print(f"Sum of squared even numbers: {even_squared_sum}")

demonstrate_stream_operations()