def win_number():
    s = 0
    f = open("example.txt", "r")
    for ln in f:
        win_lst = ln[ln.index(":") + 1:ln.index("|")].split()
        num_lst = ln[ln.index("|")+1:].split()
        n = -1
        for num in num_lst:
            if num in win_lst:
                n += 1
        s += 2 ** n if n != -1 else 0
    print(s)


def win_cards():
    card_memo = {i:1 for i in range(1, 224)}  # how many lines in the file, save time just count directly
    key = 1
    f = open("example.txt", "r")
    for ln in f:
        next_card = key + 1
        i = 0
        if card_memo[key] == 0:
            card_memo[key] = 1
        else:
            i += card_memo[key]  # get the current card number
        win_lst = ln[ln.index(":") + 1:ln.index("|")].split()
        num_lst = ln[ln.index("|")+1:].split()
        for num in num_lst:
            if num in win_lst:
                card_memo[next_card] += i
                next_card += 1
        key += 1
    print(sum(card_memo.values()))


win_number()
win_cards()