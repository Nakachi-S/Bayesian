#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2018/8/1

random_walk.py

ベイズ計算統計学のP76, 例3.5を実装する。
酔歩連鎖(random walk chain)のプログラム。

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform, norm

#採択確率を返す関数
def adoption(x, y):
    tmp = target_f(y) / target_f(x)
    
    if tmp <= 1.0:
        return(tmp)
    else:
        return(1.0)


print("ステップサイズを入力してください: 0.1 or 1 or 5")
step = float(input("σ = "))


#目標分布の設定
target_f = lambda X: (norm.pdf(X, 0, 1) / 3) + (norm.pdf(X, 4, 1) * 2 / 3)
#提案分布の設定
proposed_f = lambda X: X + uniform.rvs(loc=-step, scale=step * 2, size=1)
#サンプリング回数
N = 10000

#初期値を設定
X = 4.0
X_hist = []
cnt1 = 0 
cnt2 = 0

#サンプリング開始
for i in range(N):
    Y = proposed_f(X)
    u = uniform.rvs(loc=0, scale=1, size=1)
    if u <= adoption(X, Y):
        X_next = Y
        cnt1 += 1
    else:
        X_next = X
        cnt2 += 1
    X = X_next
    X_hist.append(float(X_next))

print("採択された数:", cnt1)
print("棄却された数:", cnt2)
print("採択確率:", cnt1 / N)


plt.figure(1)
plt.ylim(-4, 10)
plt.plot(range(10000), X_hist)
plt.show()

#目標分布の描画
plt.figure(2)
X = np.arange(-100, 100, 0.1)
Y = target_f(X)

plt.title("σ = {0}".format(step))
plt.xlim(-4, 8)
plt.ylim(0.0, 0.5)
plt.hist(X_hist, bins=50, alpha=0.5, normed=True)
plt.plot(X, Y, color="r")
plt.show()
#確かめ用
#xs = scipy.stats.uniform.rvs(loc=-step,scale=0.2,size=10000)
#plt.hist(xs, bins=50, alpha=0.5, normed=True)






