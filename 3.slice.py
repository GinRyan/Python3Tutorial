# 切片,可以操作tuple和list

nameList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
partialnameList = nameList[1:3]
print(partialnameList)

partialnameList = nameList[-3:]
print(partialnameList)

# 步进切片
partialnameList = nameList[::3]  # 所有数，每3个取1个
print(partialnameList)

partialnameList = nameList[:10:3]  # 前十个，每3个取1个
print(partialnameList)

# 字符串切片
print('ABCDEFG'[::2])

# 迭代
for namep in nameList:
    print(namep)

# 判断可迭代
from collections import Iterable
cc = isinstance('abc', Iterable)
print(cc)

#带下标迭代
for i, value in enumerate(nameList):
    print(i, ':', value)
