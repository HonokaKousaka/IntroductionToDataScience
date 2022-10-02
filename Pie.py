# Get accurate pi
import time
import random
import math

acc = round(math.pi, 8)  # 将π精确到8位小数

# 1. Monte Carlo
start = time.time()
x = random.uniform(-1, 1)
y = random.uniform(-1, 1)
total = 1
if x ** 2 + y ** 2 <= 1:
    cnt = 1
else:
    cnt = 0
while abs(cnt / total * 4 - acc) >= 1e-8:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    total += 1
    if x ** 2 + y ** 2 <= 1:
        cnt += 1
end = time.time()

print(end-start)

"""
无法判断其效率。
使用Monte Carlo方法得到的时间是不够准确的.
因为Monte Carlo方法是通过随机投点直至
计算出的π值与真实的π值的误差不超过一个限度.
而“随机投点”的过程是不能被确定的.
因此有的时候也许大部分随机投出的点在一开始就落在了圆内
而有时候大部分随机投出的点却在一开始就落在了圆外
导致了运行时间产生巨大的随机差异.
因此，其效率并不便于进行评价.
"""

# 2. arc-tan(x)
start = time.time()
res = 0
pos = 0
temp = 1
while abs(4*res-acc) >= 1e-8:
    power = (-1)**pos
    res = res + power/temp
    temp = temp + 2
    pos = pos + 1
end = time.time()
print(end-start)

# 3. 利用1/n^2求和得到π的值
start = time.time()
res = 0
temp = 1
while abs((res*6)**0.5-acc) >= 1e-8:
    res = res + 1/(temp**2)
    temp = temp + 1
end = time.time()
print(end-start)

# 4. 利用1/(2n-1)^2求和得到π的值
start = time.time()
res = 0
temp = 1
while abs((res*8)**0.5-acc) >= 1e-8:
    res = res + 1/(temp**2)
    temp = temp + 2
end = time.time()
print(end-start)

"""
第二种与第三种方法的效率类似。
第四种方法的效率相较于前两种有明显的提升。
"""