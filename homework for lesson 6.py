text = input().split()
dict1 = {}
for i in text:
    if i not in dict1:
        dict1[i] = 0
    dict1[i] += 1

sorted_dict = {}
sorted_keys = sorted(dict1, key=dict1.get, reverse=True)
for i in sorted_keys:
    sorted_dict[i] = dict1[i]
print(sorted_dict)
