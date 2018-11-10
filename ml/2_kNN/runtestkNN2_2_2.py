import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import kNN
#  2.2.2 创建散点图
fig = plt.figure()
ax = fig.add_subplot(111)
datingDataMat, datingLabels = kNN.file2matrix("./ml/2_kNN/datingTestSet2.txt")
# ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2])
ax.scatter(
    datingDataMat[:, 1],
    datingDataMat[:, 2],
    15.0 * np.array(datingLabels),
    15.0 * np.array(datingLabels),
)
plt.show()
