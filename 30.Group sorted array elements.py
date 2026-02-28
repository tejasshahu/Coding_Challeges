# Input = [1,1,1,2,2,2,3]
# Output = [[1,1,1],[2,2,2],[3]]
a = [1, 1, 2, 2, 3, 1, 2]

# 1. Create a dictionary to store our groups
groups = {}

# 2. Manually iterate through the list
for item in a:
    if item in groups:
        # If the number is already a key, add it to its list
        groups[item].append(item)
    else:
        # If it's a new number, start a new list
        groups[item] = [item]

# 3. Convert the dictionary values back into a list of lists
output = []
for key in groups:
    output.append(groups[key])

print(output)