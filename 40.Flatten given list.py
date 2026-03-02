# Flatten a nested list:
# e.g.:
input_list = ["a", "b", ["c", ["d", "e"]], "f"]
# out1 = ["a", "b", "c", "d", "e", "f"]

def flatten_list_fun(given_list):
    n = len(given_list)
    flatten_list = []
    for i in range(0, n):
        if isinstance(given_list[i], list):
            flatten_list.extend(flatten_list_fun(given_list[i]))
        else:
            flatten_list.append(given_list[i])
    return flatten_list

print(flatten_list_fun(input_list))