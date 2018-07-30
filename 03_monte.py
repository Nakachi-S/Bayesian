#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2018/7/30

03_monte.py
ロジスティック分布とコーシー分布に従う乱数を一様乱数から生成する。

今回は自分で変換した分布が合っているか調べるために、
numpyでも実行する。
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats


print("ロジスティック分布か、コーシー分布、どっちを表示させたい？\nlogistic or cauchy?")
selct = input()

if selct == "logistic":
    nbins = 50

    # ロジスティック分布のパラメータ
    mu = 0
    s = 1
    
    # 逆変換法で一様分布からロジスティック分布を得る
    np.random.seed()
    N = 100000
    U = np.random.uniform(0.0, 1.0, N)
    
    # ロジスティック分布の累積分布関数の逆関数を用いて変換
    X1 = mu + s * np.log(U / (1 - U))
    
    # 変換したロジスティック分布と理想的なpdfを描画
    plt.figure(1)
    rv = scipy.stats.logistic(loc=mu, scale=s)
    plt.hist(X1, nbins, normed=True)
    x = np.linspace(rv.ppf(0.01), rv.ppf(0.99), 1000)
    y = rv.pdf(x)
    plt.plot(x, y, 'r-', lw=2)
    plt.xlim((rv.ppf(0.01), rv.ppf(0.99)))
    
    # numpyのロジスティック分布に従う乱数生成関数を利用した場合
    plt.figure(2)
    X2 = rv.rvs(N)
    plt.hist(X2, nbins, normed=True)
    x = np.linspace(rv.ppf(0.01), rv.ppf(0.99), 1000)
    y = rv.pdf(x)
    plt.plot(x, y, 'r-', lw=2)
    plt.xlim((rv.ppf(0.01), rv.ppf(0.99)))
    
    plt.show()

elif selct == "cauchy":
    nbins = 50

    # コーシー分布のパラメータ
    x0 = 0
    gamma = 1
    
    # 逆変換法で一様分布からコーシー分布を得る
    np.random.seed()
    N = 100000
    U = np.random.uniform(0.0, 1.0, N)
    
    # コーシー分布の累積分布関数の逆関数を用いて変換
    # コーシー分布は裾野が広く極端な値も出やすいためplotするときは
    # それらのデータを切り捨てている
    X1 = x0 + gamma * np.tan(np.pi * (U - 0.5))
    X1 = X1[(X1>-10) & (X1<10)]
    
    # 変換したコーシー分布と理想的なPDFを描画
    plt.figure(1)
    rv = scipy.stats.cauchy(loc=x0, scale=gamma)
    plt.hist(X1, nbins, normed=True)
    x = np.linspace(rv.ppf(0.01), rv.ppf(0.99), 1000)
    y = rv.pdf(x)
    plt.plot(x, y, 'r-', lw=2)
    plt.xlim((-10, 10))
    
    # numpyのコーシー分布に従う乱数生成関数を利用した場合
    plt.figure(2)
    X2 = rv.rvs(N)
    X2 = X2[(X2>-10) & (X2<10)]
    plt.hist(X2, nbins, normed=True)
    x = np.linspace(-10, 10, 1000)
    y = rv.pdf(x)
    plt.plot(x, y, 'r-', lw=2)
    plt.xlim((-10, 10))
    
    plt.show()
