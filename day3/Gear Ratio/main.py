import math
import re


def switch_index(op):
    index = []
    symbols = ["@", "#", "$", "%", "-", "&", "*", "=", "+", "/"]

    f = open("string", "r")
    for ln in f:
        lst = []
        match op:
            case "sym":
                for i, x in enumerate(ln):
                    if x in symbols:
                        lst.append(i)
                index.append(lst)
            case "star":
                for i, x in enumerate(ln):
                    if x == "*":
                        lst.append(i)
                index.append(lst)
            case "num":
                it = re.finditer(r"[0-9]+", ln)
                for x in it:
                    lst.append([x.span(), x.group()])
                index.append(lst)
    return index


def match_lst(l, op):
    num_index = switch_index("num")
    res = 0
    for i, x in enumerate(l):
        if x:
            for index in x:
                lst = []
                for n in num_index[i - 1]:
                    if index - 1 - (len(n[1]) - 1) <= n[0][0] <= index + 1:
                        lst.append(int(n[1]))
                for n in num_index[i]:
                    if index - 1 - (len(n[1]) - 1) <= n[0][0] <= index + 1:
                        lst.append(int(n[1]))
                for n in num_index[i + 1]:
                    if index - 1 - (len(n[1]) - 1) <= n[0][0] <= index + 1:
                        lst.append(int(n[1]))
                match op:
                    case "add":
                        res += sum(lst)
                    case "prod":
                        if len(lst) == 2:
                            res += math.prod(lst)
    return res


def main():
    sym_index = switch_index("sym")
    star_index = switch_index("star")
    print(match_lst(sym_index, "add"))
    print(match_lst(star_index, "prod"))


main()
