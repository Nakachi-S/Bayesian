#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2018/7/31

06_monte.py
モンテカルロ積分


"""

print("今回は6つの関数を選択できるようにした\n以下から選択して。")
print("1:x^2, 2:xe^x^2, 3:x^2*e^2x, 4:logx/x, 5:x^3*logx, 6:(logx)^2")
print("数字を入力して")

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform
import scipy.integrate

select = int(input())

if select == 1:
    a, b = -1, 1
    f = lambda x: x **2

elif select == 2:
    a, b = 0, 1
    f = lambda x: x * np.exp(x**2)

elif select == 3:
    plt.xlim(0.0, 1.2)
    plt.ylim(0, 16)
    a,b = 0,1
    f = lambda x: x**2 * np.exp(2*x)

elif select == 4:
    plt.xlim(1.0, 5.0)
    plt.ylim(0.0, 0.4)
    a,b = 1, np.exp(1)
    f = lambda x: np.log(x) / x

elif select == 5:
    plt.xlim(1.0, 3.0)
    plt.ylim(-0.1, 7.0)
    a,b = 1, 2
    f = lambda x: x**3 * np.log(x)

elif select == 6:
    plt.xlim(2, 8)
    plt.ylim(0.0, 4.5)
    a,b = np.exp(1), np.exp(2)
    f = lambda x: np.log(x) ** 2

# 被積分関数をプロット
x = np.linspace(-1.5, 1.5, 1000)
y = f(x)
plt.plot(x, y)

# 積分範囲を色付け
ix = np.arange(a, b, 0.001)
iy = f(ix)
verts = [(a, 0)] + list(zip(ix, iy)) + [(b,0)]
poly = plt.Polygon(verts, facecolor='0.8', edgecolor='k')
plt.gca().add_patch(poly)

# scipy.integrateで積分を計算
I = scipy.integrate.quad(f, a, b)[0]
print ("scipy.integrate:", I)

# モンテカルロ積分
N = 100000
x = uniform(loc=a, scale=b-a).rvs(size=N)
I = (b - a) * np.mean(f(x))
print (u"モンテカルロ積分:", I)