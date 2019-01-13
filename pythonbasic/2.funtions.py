# 函数
mya = abs(-10)
print(mya)

# 定义函数


def my_Abs(x):
    if x > 0:
        return x
    else:
        return -x


myb = my_Abs(-20)
print(myb)

# 外部模块引用导入函数调用
from absdemo import myExtAbs
print(myExtAbs(-130))

# 空函数实现


def nop():
    pass


nop()

#函数多返回值
def getPoint():
    return 3, 6

x,y = getPoint()
print(x)
print(y)

#普通函数参数为位置参数
#默认参数值

def getName(name = 'sarah',age = 19):
    print(name)
    print(age)

getName('Xeros',age=79)
getName(name='John')

#默认参数的坑
def add_end(L=[]):
    L.append('END')
    return L

print(add_end([1,2,3]))

# 谁会想到[]是使用了同一个可变对象
print(add_end())
print(add_end())
print(add_end())

# 解决这个坑
def add_end_ok(L = None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end_ok())
print(add_end_ok())
print(add_end_ok())

##############

#可变参数
def calc(*numbers):
    sum =  0 
    for n in numbers:
        sum = sum + n*n
    return sum

sum = calc(1,2,3,4,5)
print(sum)

#转换List或Tuple可变参数传入
bnums = [1,2,3,4,5]
print(bnums)
print(*bnums)
print(calc(*bnums))
#转换Tuple
cnums = (1,2,3,4,5)
print(bnums)
print(*bnums)
print(calc(*bnums))

#关键字参数, 事实上是将这个参数传入Dict

def person(name,age,**keywordDict):
    #检查参数
    if 'job' in keywordDict:
        print('有job')
    if 'gender' in keywordDict:
        print('有gender')
    print('name:',name,'age:',age,'other:',keywordDict)

person('华真真',16)
person('华真真',18, gender = '女', job = '华山派弟子')

#参数类型同时存在时必须是：
#必选参数、默认参数、可变参数、命名关键字参数、关键字参数 顺序

#*后面的参数，即成为命名参数
def person2(name, age, *, city='华山', job):
    print(name, age, city, job)

person2('华真真',18,job= '华山派弟子')

#tuple和list可以作为可变参数传入， 加1个*
#dict可以作为命名参数传入，加2个*
