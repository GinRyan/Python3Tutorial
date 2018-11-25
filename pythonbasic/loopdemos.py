# loooooooop
"""5个1相加"""

totalSum = 0
for index in range(0, 5):
    totalSum += 1

"""
1+2+3+4+5
"""
totalSum1 = 0
for index in range(1, 6):
    totalSum1 += index

"""
e^x
麦克劳林公式计算e^x
"""

def calcEMaclaurin(x,k):
    totalSum = 0
    for i_of_items in range(0,k):
        fen1Mu3 = 1
        for i_of_n in range(1,i_of_items + 1):
            fen1Mu3 *= i_of_n
        latter = x**i_of_items
        totalSum += (1 / fen1Mu3) * latter
    return totalSum


# 最外层循环：累加
#       累加：依据递增的一个计数器
#       通项/重复执行的代码段(重复执行的逻辑)
#           内层循环：计数器2 外层索引值为边界
#               阶乘
#       边界条件:跳出循环的条件/不再重复的边界
#
# i = 1
#    c = 0..
# i = 2
#    c= 1...
#       ....    
    
# 练习题：
#      1、矩阵数乘 矩阵 * 实数
#      2、矩阵加法 矩阵 + 矩阵(矩阵的每一项对应相加)
#



    