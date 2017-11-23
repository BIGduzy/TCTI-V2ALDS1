def get_numbers(s):
    """
    Description
    gets all numbers in a string

    :param s: string, the string with numbers

    :return: List, the list with all numbers
    """

    numbers = []
    cur_number = ''
    for i in s:
        if i.isdigit():
            cur_number += i
        elif cur_number != '':
            numbers.append(int(cur_number))
            cur_number = ''

    if cur_number != '':
        numbers.append(int(cur_number))
    return numbers

a = '11een123zin45 6met-632meerdere+7777getallen14'
print(get_numbers(a))
