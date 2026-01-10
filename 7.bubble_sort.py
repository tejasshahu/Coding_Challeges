def bubble_sort(a):
    n = len(a)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if a[j] < a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

if __name__ == '__main__':
    a = [1,2,5,8,3]
    print(bubble_sort(a))