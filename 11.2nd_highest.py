nums = [55,32,97,-55,32,45,88,21]

def s_highest(arr_input):
    h = float("-inf")
    s_h = float("-inf")
    for i in range(0, len(arr_input)):
        if arr_input[i] > h:
            s_h = h
            h = arr_input[i]
        elif arr_input[i] >= s_h and arr_input[i] != h:
            s_h = arr_input[i]
    return h, s_h

if __name__ == '__main__':
    print("Highest & 2nd Highest:", s_highest(nums))