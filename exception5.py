def safe_divide(a, b):
    try:
        print("Result:", a / b)
    except ZeroDivisionError:
        print("Divide by zero!")
    finally:
        print("Execution complete.")

safe_divide(10, 0)