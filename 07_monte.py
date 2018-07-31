#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2018/7/31

07_monte.py
重点サンプリング(2)

"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate
from scipy.stats import norm

# 単純な重点サンプリングの例

a = 5.0

# 被積分関数
f = norm.pdf
h = lambda x: x > a
y = lambda x: h(x) * f(x)

# scipy.integrateでの積分
I1 = scipy.integrate.quad(f, a, np.inf)[0]
I2 = scipy.integrate.quad(y, -np.inf, np.inf)[0]
print ("scipy.integrate:", I1, I2)

N = 1000

# 普通のモンテカルロ積分の場合
# サンプルxを青色の標準正規分布N(x|0,1)から生成しているため
# ほとんどのサンプルが5より小さい範囲からしか生成されない
# つまり、h(x)が0となってしまう
x = norm.rvs(size=N)
I = np.mean(h(x))
print ("normal monte carlo integration:", I)

# 重点サンプリングの場合
# 重点関数g(x)として平均が5にくる正規分布N(x|5,1)を使う
g = norm(loc=5, scale=1).pdf
x = norm(loc=5, scale=1).rvs(size=N)
I = np.mean(f(x) / g(x) * h(x))
print ("importance sampling:", I)

# グラフ描画
plt.subplot(211)
ix = np.arange(-5, 15, 0.01)
plt.plot(ix, f(ix), label="f(x):normal")
plt.plot(ix, g(ix), label="g(x):normal (importance)")
plt.plot(ix, h(ix), label="h(x)")
plt.xlim((-5, 15))
plt.ylim((0, 2))
plt.legend(loc="best")

# 被積分関数yの値がある部分をズームインして表示
plt.subplot(212)
plt.plot(ix, y(ix), label="h(x)*f(x)")
plt.xlim((4.9, 7))
plt.legend(loc="best")
plt.show()