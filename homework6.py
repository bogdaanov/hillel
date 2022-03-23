import random
new_list = [1, 2, 3, 4, 5]
k = random.choice(new_list)
for i in range(k + 1, len(new_list)):
    new_list[i - 1] = new_list[i]
new_list.pop()
print(new_list)
