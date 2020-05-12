alphabet = [
    'A', 'B', 'C', 'D',	'E', 'F', 'G', 'H',	'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]


def is_number(s):
    """ Check if the number is a float """
    try:
        float(s)
        return True
    except ValueError:
        return False
    except TypeError:
        return False


def convert_cusip_to_isin(cusip):
    """ Convert cusip to isin """
    print(cusip)
    cusip = 'US' + str(cusip).upper()
    only_digits_cusip = ""
    for i in cusip:
        # print(i)
        if is_number(i):
            only_digits_cusip = str(only_digits_cusip) + str(i)
        else:
            only_digits_cusip = str(only_digits_cusip) + str(10 + alphabet.index(i))

    odd = []
    even = []

    for i, char in enumerate(only_digits_cusip):
        if i % 2 == 0:
            odd.append(char)
        else:
            even.append(char)

    new_length_list = []
    length_list = []
    string_int = ""
    if len(odd) > len(even):
        length_list = odd
        for i in even:
            string_int += str(i)
    else:
        length_list = even
        for i in odd:
            string_int += str(i)

    for i in length_list:
        new_length_list.append(int(i) * 2)

    for i in new_length_list:
        string_int += str(i)

    dig_sum = 0
    for i in string_int:
        dig_sum += int(i)

    check_sum = (10 - (dig_sum % 10)) % 10

    isin = str(cusip) + str(check_sum)

    return isin

# print(convert_cusip_to_isin('037833100'))
