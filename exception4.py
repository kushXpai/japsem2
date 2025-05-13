def open_file(filename):
    try:
        f = open(filename, 'r')
        print("File contents:", f.read())
    finally:
        print("Closing file (even if error occurs).")

open_file("non_existent_file.txt")