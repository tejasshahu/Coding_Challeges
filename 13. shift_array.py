def shift_array(n):
    temp = n[-1]
    for i in range(len(n)-2,0,-1):
        n[i+1] = n[i]
        print(n)
    n[0] = temp
    return n

if __name__ == '__main__':
    print(shift_array([4, 4, 0, 1, 1, 1, 2, 2, 3, 3]))