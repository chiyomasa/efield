import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D  # 3次元プロットのためのimport

import numpy as np

fig = plt.figure()
ax = Axes3D(fig)


LX, LY, LZ = 2, 2, 2  # xyzメッシュのパラメータ
gridwidth = 0.9
X, Y, Z = np.meshgrid(np.arange(-LX, LX, gridwidth), np.arange(-LY,
                                                               LY, gridwidth), np.arange(-LZ, LZ, gridwidth))  # メッシュ生成

R = np.sqrt(X**2+Y**2+Z**2)

#点電荷の位置座標と電荷
X1, Y1, Z1 = 0, 0, 0
Q1 = 1
R1 = np.sqrt((X-X1)**2+(Y-Y1)**2+(Z-Z1)**2)
ax.scatter3D(X1, Y1, Z1, "o", color='blue')

U = Q1*(X-X1)/(R1**2)
V = Q1*(Y-Y1)/(R1**2)
W = Q1*(Z-Z1)/(R1**2)


ax.quiver(X, Y, Z, U, V, W, color='red', length=1, normalize=False)

ax.set_xlim([-LX, LX])
ax.set_ylim([-LY, LY])
ax.set_zlim([-LZ, LZ])
plt.show()
