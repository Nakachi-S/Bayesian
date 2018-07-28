#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 19:15:22 2018

01_monte.py
http://aidiary.hatenablog.com/entry/20140620/1403272044
上のURLを参考にモンテカルロ法に関するプログラムを作る。

一様乱数の生成のプログラム
"""

#一様乱数の生成してヒストグラムを描画
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 8)
np.random.seed()
N = 10000
x = np.random.uniform(0.0, 1.0, N)
nbins = 100
plt.hist(x, nbins, normed=True)
plt.show()

from scipy.stats import uniform

#一様分布に従う確率分布からランダムサンプリング
np.random.seed()
#[0.0, 1.0]の一様分布に従う確率変数
rv = uniform(loc=0.0, scale=1.0)
#一様分布からサンプリング
x = rv.rvs(size=N)
plt.hist(x, nbins, normed=True)

#真のPDFを描画
x = np.linspace(rv.pdf(0), rv.pdf(1), 100)
plt.plot(x, uniform.pdf(x), 'r-', lw=2, label='uniform pdf')

plt.show()

