from numpy import *
import operator
import numpy as np


def createDataset():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ["A", "A", "B", "B"]

    return group, labels


def classify0(inX: array, dataSet: array, labels: array, k: int):
    dataSetSize: int = dataSet.shape[0]  # 确定数据集大小
    tileInputX: array = tile(inX, (dataSetSize, 1))  # 延展数据集, 将输入向量inX重复n行1列，n等于数据集大小
    diffMat: array = tileInputX - dataSet  # 求坐标差
    sqDiffMat: array = diffMat ** 2  # 坐标差的每个指标值的平方
    sqDistances = sqDiffMat.sum(axis=1)  # 然后求和

    distances = sqDistances ** 0.5  # 开方
    sortedDistIndices = distances.argsort()
    classCount = {}
    for i in range(k):
        voteILabel = labels[sortedDistIndices[i]]
        classCount[voteILabel] = classCount.get(voteILabel, 0) + 1
    sortedClassCount = sorted(
        classCount.items(), key=operator.itemgetter(1), reverse=True
    )

    return sortedClassCount[0][0]


def file2matrix(filename):
    #只读模式打开文件 "r"只读模式
    fr = open(filename, "r")
    #读入文件所有行
    arrayOLines = fr.readlines()
    #识别共有多少行数
    numberOfLines = len(arrayOLines)
    #根据文件的行数和3列数构建一个全零矩阵，用于装载文件中的前三列数据
    returnMat = np.zeros((numberOfLines, 3))
    # 记录标签列向量(下面通过获取每行最后一列数作为标签列向量)，用于装载文件中第四列类别标签
    classLabelVector = []
    index = 0 #
    #开始遍历每一行数据
    for line in arrayOLines:
        #strip()砍掉了这个字符串头部和尾部的空格和回车，因为空格和回车没有任何毛用处
        line = line.strip()
        #split把一个字符串以\t为分隔符，分割成好几个字符串的数组，也就是说listFromLine是一个保存了好几个字符串的数组
        #比如说第一行数据：40920	8.326976	0.953952	3
        #数字之间是用的制表符\t分隔的，那么split方法传入\t，告知以\t作为分节符号切分，切分成字符串数组
        #切分成["40920","8.326976","0.953952","3"]保存在listFromLine中
        listFromLine = line.split("\t")
        #在returnMat中的第index列开始，保存从文件中读取的数据的前三列数据集
        #因为数据集文件的前三列是数据，最后一列是结果标签
        #按照上面的例子，是保存了["40920","8.326976","0.953952"]到returnMat[index]
        returnMat[index] = listFromLine[0:3]
        #类别标签向量，每一次循环都把listFromLine切分的最后一个值转换成整型值，追加到classLabelVector
        #按照上面举得例子，是把3追加到classLabelVector后面
        classLabelVector.append(int(listFromLine[-1]))
        #递增索引，用于读取下一行,直到最后行数值numberOfLines
        index += 1
    #返回数据集矩阵以及结果集标签向量
    return returnMat, classLabelVector

#import matplotlib.pyplot as plt



