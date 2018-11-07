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
    sqDiffMat: array = diffMat ** 2  #坐标差的每个指标值的平方
    sqDistances = sqDiffMat.sum(axis=1) #然后求和

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

