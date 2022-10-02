# 循环迭代，逐步逼近
i = 1
while 2 - i ** 2 >= 0.0001:
    i = i + 0.00001
print(i)

# 二分查找，折半返回
minNum = 0
maxNum = 2
i = 1
while abs(2 - i ** 2) >= 0.0001:
    i = (minNum + maxNum) / 2
    if i**2 < 2:
        minNum = i
    else:
        maxNum = i

print(i)

# 曲线切线，线性逼近
g = 1
while abs(2 - g ** 2) >= 0.0001:
    g = (g + 2/g) / 2
print(g)
