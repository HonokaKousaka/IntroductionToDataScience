lst = [1, 2, 3, 4, 5]

for i in range(4, -1, -1):
    print(lst[i], end=" ")

i = 4
while i >= 0:
    print(lst[i], end=" ")
    i -= 1

reverse = lst[-1:-6:-1]
for i in reverse:
    print(i, end=" ")
