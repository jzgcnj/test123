import matplotlib.pyplot as mp
import numpy as np

# 饼图pie
mp.figure('PIE',facecolor='lightgray')
mp.title('PIE',fontsize=20)

# 绘制饼图所需参数
value = [26,17,21,29,11] # 值
spaces = [0.05,0.01,0.01,0.01,0.01] # 扇形之间的间距
labels = ['Python','JavaScript','C++','Java','PHP'] # 对应各个值得标签
colors = ['dodgerblue','orangered','limegreen','violet','gold'] # 对应各个值的颜色

# %1f%%，百分数显示格式，%%代表加一个百分号，.1f浮点数保留一位小数
mp.pie(value,spaces,labels,colors,'%.1f%%',shadow=True)
mp.axis('equal') # 等轴比例（x轴与y轴等比例），显示出来就是一个正圆，否则默认是椭圆
mp.legend()
mp.show()