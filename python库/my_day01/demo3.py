## 绘制10-12点气温

import matplotlib.pyplot as plt
import random

plt.figure(figsize=(20,10),dpi=80)

x=range(0,120)
## 循环120次，每次取随机数
y=[random.randint(20,35) for i in range(120)]

plt.plot(x,y)

plt.show()
