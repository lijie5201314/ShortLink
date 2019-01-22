from math import pow

NUMBER_ARR = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
              'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def _10_to_62(number):
    return ten_to_weight(number, 62, NUMBER_ARR)




def ten_to_weight(number, weight, mapping_table=None):
    if number == 0:
        return 0
    rest = int(number)
    res = []
    if mapping_table:
        while rest != 0:
            shang, mod = divmod(rest, weight)
            res.insert(0, NUMBER_ARR[mod])
            rest = shang
    else:
        while rest != 0:
            shang, mod = divmod(rest, weight)
            res.insert(0, str(mod))
            rest = shang
    return ''.join(res)


if __name__ == '__main__':
    print(_10_to_62('11'))

