#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2018/7/30

02_monte.py
逆変換法
逆変換方と[0,1]区間の一様分布から得られた乱数を
変換することで任意の確率分布に従う乱数を得る手法。

今回は指数分布に従う乱数を生成。
"""

#逆変換法で一様分布から指数分布を得る
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

nbins = 50

# 指数分布のパラメータ（scale = 1/lambda）
scale = 1.0

# 逆変換法で一様乱数から指数分布の乱数を得る
np.random.seed()
N = 100000
U = scipy.stats.uniform(loc=0.0, scale=1.0).rvs(size=N)

# 指数分布の累積分布関数の逆関数を用いて変換
X1 = - scale * np.log(1 - U)

# 生成した元の一様乱数を描画
plt.figure(1)
plt.hist(U, nbins, normed=True)

# 変換した指数分布の乱数と理想的なPDFを描画
plt.figure(2)
rv = scipy.stats.expon(scale=scale)
plt.hist(X1, nbins, normed=True)
x = np.linspace(rv.ppf(0.01), rv.ppf(0.99), 1000)
y = rv.pdf(x)
plt.plot(x, y, 'r-', lw=2, label = "expon")
plt.xlim((rv.ppf(0.01), rv.ppf(0.99)))
plt.legend()
plt.show()