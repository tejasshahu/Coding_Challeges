def bubble_sort(a):
    n = len(a)
    for i in range(n-2,-1,-1):
        is_swap = False
        for j in range(0,i+1):
            if a[j] < a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                is_swap = True
        if is_swap is False:
            break
    return a

if __name__ == '__main__':
    a = [1,2,5,8,3]
    print(bubble_sort(a))