def access_list_element(lst, index):
    try:
        print("Element:", lst[index])
    except IndexError:
        print("Error: Index out of range.")
    except TypeError:
        print("Error: Invalid input type.")

access_list_element([1, 2, 3], 'a')