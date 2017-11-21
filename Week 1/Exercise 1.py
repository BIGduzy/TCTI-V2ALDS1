def my_max(a):
    """
    description
    Prints maximum value in list, raises error when list length < 1 or list contains non-numeric

    Parameters
    ----------
    a : List
    list with numbers
    """

    if len(a) == 0:
        raise ValueError("Invalid array length")

    max_value = a[0]
    for i in a:
        if type(i) != int and type(i) != float:
            raise ValueError("List contains non-numeric")

        if i > max_value:
            max_value = i

    print(max_value)


my_max([1, -2, 21, 6, 3, 4])
my_max([-1, -2, -21, -6, -3, -4])
# my_max([])
# my_max([1, 2, 1, '6', 3])
