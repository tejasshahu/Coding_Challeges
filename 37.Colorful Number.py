"""
A number can be broken into different contiguous sub - subsequence parts.
Suppose, a number 3245 can be broken into parts like
3 -> 3
2 -> 2
4 -> 4
5 -> 5
32 -> 6
24 -> 8
45 ->20
324 -> 24
245 -> 40
And this number is a COLORFUL number,

Example 2:
since product of every digit of a
contiguous subsequence is different.
A = 237
2 -> 2
3 -> 3
7 -> 7
23 -> 6
37 -> 21

Example 3:
213
2->2
1->1
3->3
21->2
1 * 3->3
"""
# def get_num_split(num):
#     num_list = []
#     while num > 9:
#         a = num%10
#         num_list.append(a)
#         num = num//10
#     num_list.append(num)
#     num_list.reverse()
#     return num_list

def is_colorful(num):
    s = str(num)
    products = set()
    for i in range(len(s)):
        product = 1
        for j in range(i, len(s)):
            digit = int(s[j])
            product *= digit
            if product in products:
                return False
            products.add(product)
    return True
print(is_colorful(237))