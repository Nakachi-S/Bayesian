#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2018/7/27

01_monte.py
http://aidiary.hatenablog.com/entry/20140620/1403272044
上のURLを参考にモンテカルロ法に関するプログラムを作る。

一様乱数(Uniform distribution)の生成のプログラム
"""

#一様乱数の生成してヒストグラムを描画
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

print("numpy or scipy?")
selct = input()

#numpyを使って一様乱数の生成
if selct == "numpy":
    #plt.rcParams['figure.figsize'] = (10, 10)
    np.random.seed()
    N = 10000
    x = np.random.uniform(0.0, 1.0, N)
    nbins = 50
    plt.hist(x, nbins, normed=True, label="frozen pdf")
    plt.show()

#scipy.stats用いて一様乱数の生成
if selct == "scipy":
    #一様分布に従う確率分布からランダムサンプリング
    np.random.seed()
    N = 10000
    #[0.0, 1.0]の一様分布に従う確率変数
    rv = uniform(loc=0.0, scale=1.0)
    #一様分布からサンプリング
    x = rv.rvs(size=N)
    nbins = 50
    plt.hist(x, nbins, normed=True, label='frozen pdf')
    
    #真のPDFを描画
    x = np.linspace(uniform.ppf(0.01), uniform.ppf(0.99), 100)    
    plt.plot(x, uniform.pdf(x), 'r-', lw=4, label='uniform pdf')    #lwは線の太さ
    plt.legend()
    plt.show()

