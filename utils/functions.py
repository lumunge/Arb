import itertools


def color(text, r, g, b):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


def probability(a, b, c):
    if round((((1 / a) + (1 / b) + (1 / c)) * 100), 2) < 100:
        return color(round((((1 / a) + (1 / b) + (1 / c)) * 100), 2), 127, 255, 0)
    return ""


def genIndices():
    ll = [[2, 5, 8, 11, 14], [3, 6, 9, 12, 15], [4, 7, 10, 13, 16]]
    finalList = list(itertools.product(*ll))
    finale = list()
    for i in finalList:
        if ll[0][0] in i and ll[1][0] in i and ll[2][0] in i:
            continue
        elif ll[0][1] in i and ll[1][1] in i and ll[2][1] in i:
            continue
        elif ll[0][2] in i and ll[1][2] in i and ll[2][2] in i:
            continue
        elif ll[0][3] in i and ll[1][3] in i and ll[2][3] in i:
            continue
        elif ll[0][4] in i and ll[1][4] in i and ll[2][4] in i:
            continue
        elif ll[0][0] in i and ll[1][0] in i:
            continue
        elif ll[0][1] in i and ll[1][1] in i:
            continue
        elif ll[0][2] in i and ll[1][2] in i:
            continue
        elif ll[0][3] in i and ll[1][3] in i:
            continue
        elif ll[0][4] in i and ll[1][4] in i:
            continue
        elif ll[0][0] in i and ll[2][0] in i:
            continue
        elif ll[0][1] in i and ll[2][1] in i:
            continue
        elif ll[0][2] in i and ll[2][2] in i:
            continue
        elif ll[0][3] in i and ll[2][3] in i:
            continue
        elif ll[0][4] in i and ll[2][4] in i:
            continue
        elif ll[1][0] in i and ll[2][0] in i:
            continue
        elif ll[1][1] in i and ll[2][1] in i:
            continue
        elif ll[1][2] in i and ll[2][2] in i:
            continue
        elif ll[1][3] in i and ll[2][3] in i:
            continue
        elif ll[1][4] in i and ll[2][4] in i:
            continue
        else:
            finale.append(i)
    return finale
