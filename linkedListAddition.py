def listAddition(l1, l2):
    l1_rev_str = ''
    l2_rev_str = ''
    for i in reversed(l1):
        l1_rev_str += str(i)
    for i in reversed(l2):
        l2_rev_str += str(i)
    return int(l1_rev_str + l2_rev_str)

if __name__ == '__main__':
    l1, l2 = [2, 4, 3], [5, 6, 4]
    print(listAddition(l1, l2))