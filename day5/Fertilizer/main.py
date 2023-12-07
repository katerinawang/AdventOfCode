from itertools import groupby


def split(op):
    return_lst = []
    f = open("seeds", "r")
    lst = [ln.rstrip() for ln in f]
    seed_route = [list(c) for i, c in groupby(lst, key=bool) if i]
    f.close()

    match op:
        case "new":
            s = seed_route[0][0]
            lst = s[s.index(":") + 1:].split()
            for i in range(0, len(lst), 2):
                return_lst.append([lst[i], lst[i + 1]])
        case "seeds":
            s = seed_route[0][0]
            return_lst = s[s.index(":") + 1:].split()
        case "sts":
            return_lst = seed_route[1]
        case "stf":
            return_lst = seed_route[2]
        case "ftw":
            return_lst = seed_route[3]
        case "wtl":
            return_lst = seed_route[4]
        case "ltt":
            return_lst = seed_route[5]
        case "tth":
            return_lst = seed_route[6]
        case "htl":
            return_lst = seed_route[7]
        case "":
            print(seed_route[1])
            print(len(seed_route))
    return return_lst


def find_route(source, string):
    route = -1
    map_lst = string.split()
    diff = int(source) - int(map_lst[1])
    if 0 <= diff < int(map_lst[2]):
        route = int(map_lst[0]) + diff
    return route


def get_route(lst):
    return lst[1:]


def get_next_num(source, lst):
    num = -1
    for route in lst:
        if num != -1:
            break
        num = find_route(source, route)
    if num == -1:
        num = source
    return int(num)


def get_location(seed):
    sts = get_route(split("sts"))
    stf = get_route(split("stf"))
    ftw = get_route(split("ftw"))
    wtl = get_route(split("wtl"))
    ltt = get_route(split("ltt"))
    tth = get_route(split("tth"))
    htl = get_route(split("htl"))

    destination = get_next_num(seed, sts)
    destination = get_next_num(destination, stf)
    destination = get_next_num(destination, ftw)
    destination = get_next_num(destination, wtl)
    destination = get_next_num(destination, ltt)
    destination = get_next_num(destination, tth)
    destination = get_next_num(destination, htl)

    return destination


def lowest(lst):
    low = 0
    for i, seed in enumerate(lst):
        num = get_location(seed)
        if i == 0 or low > num:
            low = num
    return low


def main():
    single_seed = split("seeds")
    print(lowest(single_seed))


main()
