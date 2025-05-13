def convert_to_int(s):
    try:
        num = int(s)
    except ValueError:
        print("Error: Not a valid integer.")
    else:
        print("Conversion successful:", num)

convert_to_int("123")
convert_to_int("abc")