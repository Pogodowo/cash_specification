def sumstr(str):
    s = ''

    str = str.split()
    print(str)
    a = 0
    for i in range(0, len(str)):
        s = s + ' ' + str[i]
        if i > 0 and (i + 1) % 5 == 0:
            s = s + '\n'
    if s and s[-1] == '\n':
        return s[:-1]
    else:
        return s


def sumpdf(str):
    s = ''
    str = str.split()
    for i in range(0, len(str)):
        s = s + ' ' + str[i]

        if i > 0 and (i + 1) % 5 == 0:
            s = s + '\n'
    return s