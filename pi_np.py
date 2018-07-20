#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pi_np.py

モンテカルロ法を用いて、円周率の算出を行う
numpyを用いて行う
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
#matplotlib inline
plt.rcParams['figure.figsize'] = (10, 10)

x = np.arange(0, 1.01, 0.01)
y = np.sqrt(1 - x ** 2)
plt.plot(x, y, c='g')
plt.xlim(0,1)
plt.ylim(0,1)
# モンテカルロ法による円周率の導出
n = 10_000
x = np.random.rand(n)
y = np.random.rand(n)
cond = x ** 2 + y ** 2 <= 1
c = len(x[cond])
plt.scatter(x[~cond], y[~cond], c='r')
plt.scatter(x[cond], y[cond], c='b')
print('count: {0}, Π = {1}'.format(c, float(c) / n * 4))