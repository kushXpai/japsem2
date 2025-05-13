def demonstrate_lambda():
    add = lambda x, y: x + y
    square = lambda x: x * x
    greet = lambda name: f"Hello, {name}"

    print("Lambda Expressions:")
    print(f"Add 5 and 3: {add(5, 3)}")
    print(f"Square of 4: {square(4)}")
    print(f"Greet 'Alice': {greet('Alice')}")

demonstrate_lambda()