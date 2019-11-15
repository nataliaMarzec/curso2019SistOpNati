
def qsort(arr, comp):
    less = []
    pivot_list = []
    more = []

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]

        for elem in arr:
            if comp(elem, pivot) == -1:
                less.append(elem)
            elif comp(elem, pivot) == 1:
                more.append(elem)
            else:
                pivot_list.append(elem)

        less = qsort(less, comp)
        more = qsort(more, comp)

        return less + pivot_list + more


def f(a, b):
    if len(a) < len(b):
        return -1
    elif len(a) > len(b):
        return 1
    else:
        return 0
