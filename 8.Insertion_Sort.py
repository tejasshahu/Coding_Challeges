def insertion_sort(a):
    n = len(a)
    for i in range(1,n):
        k = a[i]
        j = i - 1
        while j >= 0 and a[j] < k:
            a[j+1] = a[j]
            a[j] = k
            j -= 1
    return a

if __name__ == '__main__':
    a = [1,2,5,8,3]
    print(insertion_sort(a))