import numpy as np
import matplotlib.pyplot as plt

#生成序列数据

x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

#绘制sin和cos
plt.plot(x,y1,label="sin",linestyle="-")
plt.plot(x,y2,label="cos", linestyle="--")

plt.xlabel("x")
plt.ylabel("y")

plt.title("sin & cos")
plt.legend()

plt.show()

