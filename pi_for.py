#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pi_for.py

モンテカルロ法を用いて、円周率の算出を行う
for文を用いて行う
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
c = 0
n = 1000
for i in range(0, n):
    x = np.random.rand()
    y = np.random.rand()
    if x ** 2 + y ** 2 <= 1:
        plt.scatter(x, y, c='b')
        c += 1
    else:
            plt.scatter(x, y, c='r')
print('count: {0}, Π = {1}'.format(c, float(c) / n * 4))