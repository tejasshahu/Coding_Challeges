def reverse_arr(array_list, l ,r):
    while l<=r:
        array_list[l], array_list[r] = array_list[r], array_list[l]
        l += 1
        r -= 1
        reverse_arr(array_list, l, r)
    return array_list

if __name__ == '__main__':
    input_array = [1, 2, 3, 4, 5, 9 ,10,11]
    start = 3
    end = 5
    print(reverse_arr(input_array, start, end))