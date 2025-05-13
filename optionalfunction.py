from typing import Optional

def demonstrate_optional():
    value: Optional[int] = None
    another_value: Optional[int] = 42

    print("\nOptional Demonstration:")
    print(f"Value is present: {value is not None}")
    print(f"Another value is present: {another_value is not None}")

    print(f"Value or default 10: {value if value is not None else 10}")
    print(f"Another value or default 10: {another_value if another_value is not None else 10}")

demonstrate_optional()