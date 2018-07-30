#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2018/7/30

04_monte.py
受理・棄却法

"""

# ベータ乱数を受理・棄却法で生成
# 目標分布（ここではベータ分布）のpdfは既知とする
# 提案分布として一様分布を使用

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
from scipy.stats import uniform, beta

np.random.seed()

# 目標分布f
f = beta(a=2.7, b=6.3).pdf

# 提案分布g
# 提案分布から乱数生成するためにgvも保持
gv = uniform
g = gv.pdf

# 分布の上限を指定する定数Mを設定
# ベータ分布のpdfの上限値を指定すればベータ分布をすべて覆える
# 最大値を求めるためにベータ分布のpdfにマイナスをつけて
# 最小値問題に帰着させる
xopt = scipy.optimize.fmin(lambda x: -f(x), 0.0, disp=False)
M = f(xopt)[0]
print ("M =", M)

# 受理・棄却法
Nsim = 100000

# 提案分布gからの乱数Yを生成
Y = gv.rvs(size=Nsim)

# 一様乱数UをNsim個生成
U = uniform.rvs(size=Nsim)

# Yから受理の条件を満たすサンプルXを残して残りを棄却
X = Y[U <= f(Y) / (M * g(Y))]
print (u"サンプル数: %d => %d" % (len(Y), len(X)))
print (u"実際の受理率  : %f" % (len(X) / float(len(Y))))
print (u"理論的な受理率: %f" % (1.0 / M))

# 目標分布を描画
x = np.linspace(0.0, 1.0, 1000)
y = f(x)
plt.plot(x, y, 'r-', lw=2)

# 提案分布（一様分布）を描画
y = M * uniform.pdf(x)
plt.plot(x, y, 'g-', lw=2)

# 受理した乱数の分布を描画
plt.hist(X, bins=50, normed=True)

plt.show()



# 受理されたサンプルと棄却されたサンプルを描く
# 点の数が多すぎるのでNsimを小さくした

# 目標分布f
f = beta(a=2.7, b=6.3).pdf

# 提案分布g
# 提案分布から乱数生成するためにgvも保持
gv = uniform
g = gv.pdf

Nsim = 2000

# 候補密度からの乱数Yを生成
Y = uniform.rvs(size=Nsim)

# 一様乱数UをNsim個生成
U = uniform.rvs(size=Nsim)

# 受理されたサンプルと、棄却されたサンプルのインデックスを計算
acceptedIdx = U <= f(Y) / (M * g(Y))
rejectedIdx = U > f(Y) / (M * g(Y))

# 目標分布を描画
x = np.linspace(0.0, 1.0, 1000)
y = f(x)
plt.plot(x, y, 'r-', lw=2)

# 提案分布を描画
y = M * g(x)
plt.plot(x, y, 'g-', lw=2)

# 受理されたサンプルを描画
plt.scatter(Y[acceptedIdx], U[acceptedIdx] * M * g(Y[acceptedIdx]), color="red")
plt.scatter(Y[rejectedIdx], U[rejectedIdx] * M * g(Y[rejectedIdx]), color="blue")

plt.xlim((0.0, 1.0))
plt.ylim((0.0, 3.0))

plt.show()