#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 数字类型
a = 1
print(1)

# 字符串
myStr = "ABC"
print(myStr)

aunicode = 'ABC'.encode('GBK')
print(aunicode)

# 输入
#name = input("请输入您的姓名")
#print (name)

# 多行
print('''多行
引号''')

# 原始字符串
print(r'''原始字
符串''')

# 逻辑运算符
bValue = True
bValue1 = False
print(bValue)
print(bValue and bValue1)
print(bValue or bValue1)
print(not bValue1)

# 精确除法
print(10 / 3)
print(10 // 3)

# 取余数
print(10 % 3)

# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print(ord("汉"))
print(chr(27777))

# \u输入unicode
ch_u = '\u4e2d\u6587'
print(ch_u)

# 指定编码
set_charactor = r"中文编码"
print(set_charactor.encode('utf-8'))
print(set_charactor.encode('gbk'))

# 忽略错误
ig = b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
print(ig)

length = len(set_charactor)
print(length)

# 格式化输出，如果要表示%在字符串，那么就用%%转义为%
print('Hi, %s, you have $%d. 占用%s%%' % ('Michael', 1000000, 16))

# format函数, .1f 表示 浮点类型保留小数点后1位
print('{0}成绩上涨了{1:.1f}%'.format("小明", 18.565))

# 列表list
myClass = ["小明", "小王", "小绿"]
print(myClass)
print(myClass[1])
print(myClass[-1])
myClass.append("阿豪")
print(myClass)
myClass.insert(2, '阿六')
print(myClass)
myClass.pop(2)
print(myClass)

mL = ['String', 12, False, ["Facebook", "Google"]]
print(mL)
print(mL[3][1])
print(len(mL))

# 元组tuple，有序列表
myClassMates = ("大宝", "二宝")
print(myClassMates)

# 条件判断
age = 18
#age = int(ageStr)

if age == 18:
    print('刚刚成年')
elif age < 18 and age > 0:
    print('未成年')
elif age > 18:
    print('成年了，可以XXX了')
else:
    print('没出生吧')


# for 循环 range范围
names = ['大宝', '二宝', '三宝']
for name in names:
    print(name)

ab = list(range(6))
for aitem in ab:
    print(aitem)

# while

v = 1
while v < 6 and v > 0:
    v = v + 1
    print(v)


# Dict Set，必须都是不可变对象
# Dict
memscores = {'李红袖': 95, '苏蓉蓉': 99, '宋甜儿': 93, '无花': 60, '快网张三': 90}
print(memscores['李红袖'])
print(memscores)

memscores['李红袖'] = 97
print(memscores['李红袖'])
print(memscores)

lihongxiuExist = '李红袖' in memscores
print(lihongxiuExist)

memscores.pop('无花')
print(memscores)

# Set 非重复元素集合
s = set([1, 1, 2, 3, 4, 5])
print(s)
s.add(90)
print(s)
s.remove(90)

# 集合的数学操作
s2 = set([3, 8, 11, 14])
print(s & s2)
print(s | s2)

