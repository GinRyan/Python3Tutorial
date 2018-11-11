import kNN

dateDataMat,labels = kNN.file2matrix('./ml/2_kNN/datingTestSet2.txt')
normMat,ranges,minVals = kNN.autoNorm(dateDataMat)
print(normMat[0:0,2:2])
print(ranges)
print(minVals)