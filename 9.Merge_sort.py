def merge_array(l, r):
    merged_arr = []
    m = len(l)
    n = len(r)
    i = 0
    j = 0
    while i < m and j < n:
        if l[i] < r[j]:
            merged_arr.append(l[i])
            i += 1
        else:
            merged_arr.append(r[j])
            j += 1
    while i < m:
        merged_arr.append(l[i])
        i += 1
    while j < n:
        merged_arr.append(r[j])
        j += 1
    return merged_arr


def merge_sort(a):
    if len(a) == 1:
        return a
    divide = len(a) // 2
    left = a[:divide]
    right = a[divide:]
    l = merge_sort(left)
    r = merge_sort(right)
    return merge_array(l, r)

if __name__ == '__main__':
    a = [1,2,5,8,3]
    print(merge_sort(a))