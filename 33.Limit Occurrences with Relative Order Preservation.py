# input = [1,1,1,2,2,3,1,2]
# output = [1,1,2,2,3,1,2]
# k = 2
# 1ts iteration: [1,1,2,2,2,3,1]
# 2nd iteration: [1,1,2,2,3,1,2]

input_list = [1, 1, 1, 2, 2, 2, 3, 3, 1, 2]
k = 2
# Output: [1, 1, 2, 2, 3, 3, 1, 2, 1, 2]

def solve(arr, k):
    counts = {}
    i = 0
    moves_made = 0
    original_length = len(arr)

    # We only need to process the original elements once
    while i < (original_length - moves_made):
        val = arr[i]

        # Update our manual counter
        if val in counts:
            counts[val] += 1
        else:
            counts[val] = 1

        # If count exceeds k, move it to the end
        if counts[val] > k:
            # 1. Remove the element at the current index
            popped_val = arr.pop(i)
            # 2. Append it to the very end
            arr.append(popped_val)
            # 3. Reduce the count for this instance since it's "moved"
            # (or keep it if you want to count the moved ones too)
            counts[val] -= 1
            # 4. Record that we moved one so we don't loop forever
            moves_made += 1
            # Note: We do NOT increment 'i' because a new element shifted into this index
        else:
            i += 1

    return arr


output = solve(input_list, k)
print(f"Result: {output}")
# Output: [1, 1, 2, 2, 3, 3, 1, 2, 1, 2]