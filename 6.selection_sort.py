def selection_sort(a):
    for i in range(0, len(a)):
        max_index = i
        for j in range(i+1, len(a)):
            if a[j] > a[max_index]:
                a[i], a[j] = a[j], a[max_index]
    return a


if __name__ == '__main__':
    a = [1,2,5,8,3,1,7]
    print(selection_sort(a))