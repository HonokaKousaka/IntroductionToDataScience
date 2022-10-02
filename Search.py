string = input()
p = 0
maxNum = 0
length = len(string)
for i in range(length - 1):
    if string[i] == string[i + 1]:
        cnt = 1
        p = 1
        for j in range(i + 1, length - 1):
            if string[j] == string[i]:
                cnt = cnt + 1
            else:
                if maxNum < cnt:
                    maxNum = cnt
                break

if p == 1:
    print("Exist")
    print(maxNum)
else:
    print("Not Exist")
