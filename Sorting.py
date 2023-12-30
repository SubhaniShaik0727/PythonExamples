pos = -1


def search(plist, pn):
    low = 0
    upper = len(plist)-1
    while low <= upper:
        mid = (low+upper) // 2
        if plist[mid] == pn:
            globals()['pos'] = mid
            return True
        else:
            if plist[mid] < n:
                low = mid + 1
            else:
                upper = mid - 1

        return False


new_list = [67, 87, 90, 10, 20, 45, 66]
n = 10
if search(new_list, n):
    print("Found at", pos + 1)
else:
    print("Not Found")

