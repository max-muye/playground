import matplotlib.pyplot as plt
import numpy as np

# 创建x轴数据点
x = np.linspace(-2, 2, 1000)
# 计算y=x^3
y = x**3

# 创建图形和轴
plt.figure(figsize=(10, 10))
plt.grid(True)
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)

# 绘制函数图像
plt.plot(x, y, 'b-', label='y=x^3')

# 设置x和y轴使用相同的比例尺度
plt.axis('equal')

plt.title('y=x^3')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# 显示图像
plt.show()