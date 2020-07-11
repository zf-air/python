## 绘制24小时气温

import matplotlib.pyplot as plt

x=range(2,26,2)
y=[15,13,14.5,17,20,25,26,26,24,22,18,15]

## 设置图片格式
plt.figure(figsize=(20,10),dpi=80)

plt.plot(x,y)

## 设置x轴间距
# 初始的
plt.xticks(x)

# 间距为1
# _xticks_labels=[i/2 for i in range(4,49)]
# plt.xticks(_xticks_labels)


## 设置y轴间距,最小和最大即可
plt.yticks(range(min(y),max(y)+1))


## 保存图片
# plt.savefig("./my_day01/sig_size.png")

## show要放在save前面
plt.show()
