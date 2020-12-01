import numpy as np
import matplotlib.pyplot as plt
import math

# const
Q = ((0.0, 0.0), 10.0), ((5.0, -5.0), 5.0)  # 電荷の位置と値

TIMELIMIT = 20.0

RLIMIT = 0.1  # 距離rの最低値
H = 0.01

# main
t = 0.0

# input coefficient

vx = float(input("input initial v0x:"))
vy = float(input("input initial v0y:"))
x = float(input("input initial x:"))
y = float(input("input initial y:"))

print("{:.7f} {:.7f} {:.7f} {:.7f} {:.7f}".format(t, x, y, vx, vy))

# グラフデータに位置を追加

xlist = [x]
ylist = [y]


# calculation

while t < TIMELIMIT:
    t = t + H
    rmin = float("inf")  # initialize min distanve
    for qi in Q:
        rx = qi[0][0] - x  # r=rx
        ry = qi[0][1] - y  # r=ry
        r = math.sqrt(rx * rx + ry * ry)  # calculate r
        if r < rmin:
            rmin = r  # update r min
        vx += (rx / r / r / r * qi[1]) * H  # calculate vx
        vy += (ry / r / r / r * qi[1]) * H  # calculate vx
    x += vx * H  # calculate x
    y += vy * H  # calculate y
    print("{:.7f} {:.7f} {:.7f} {:.7f} {:.7f}".format(t, x, y, vx, vy))

    # グラフデータに位置を追加
    xlist.append(x)
    ylist.append(y)

    if rmin < RLIMIT:
        break  # 電荷が近傍であれば終了

# グラフの表示
plt.plot(xlist, ylist)
plt.show()
