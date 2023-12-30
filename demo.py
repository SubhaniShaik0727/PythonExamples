pos = -1


def search(plist, pn):
    i = 0
    while i < len(plist):
        if plist[i] == pn:
            globals()['pos'] = i
            return True
        i = i + 1
    return False


new_list = [10, 20, 30, 40, 22]
n = 30
if search(new_list, n):
    print("Found", pos + 1)
else:
    print("Not Found")
