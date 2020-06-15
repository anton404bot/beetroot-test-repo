def get_largest(num):
    list_for_nums = sorted([int(i) for i in str(num)], reverse=True)
    result = ''
    for i in list_for_nums:
        result += str(i)
    return int(result)


def convert_list(list):
    s = [str(i) for i in list]
    res = int(''.join(s))
    return res

