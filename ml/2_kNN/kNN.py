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
    fr = open(filename, "r")#打开文件 
    arrayOLines = fr.readlines()#读入文件所有行
    numberOfLines = len(arrayOLines)#识别行数
    returnMat = np.zeros((numberOfLines, 3))#根据文件的行数和3列数构建一个全零矩阵
    classLabelVector = []# 记录标签列向量(下面通过获取每行最后一列数作为标签列向量)
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split("\t")
        returnMat[index] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector

#import matplotlib.pyplot as plt



