#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 13:52:57 2018

@author: julianissen
"""
import Fraction_model_temp as temp_model
import Fraction_model as frac_model
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize = (15,15))
ax1 = fig.add_subplot(1,1,1)


x1_lim = [-0.5, 14]
y1_lim = [-0.045, 0.036]


model1 = temp_model.sourceTempChange(25.13, 1.25, -7.92, -7.87, 68, ax1, x1_lim, y1_lim)
model1.T_function_interglacial()

y1_major_ticks = np.arange(-0.045, 0.036, 0.02)
y1_minor_ticks = np.arange(-0.045, 0.036, 0.01)
x1_major_ticks = np.arange(0, 13.3, 2)
x1_minor_ticks = np.arange(0, 13.3, 1)

ax1.set_yticks(y1_major_ticks)
ax1.set_yticks(y1_minor_ticks, minor=True)
ax1.set_xticks(x1_major_ticks)
ax1.set_xticks(x1_minor_ticks, minor=True)

for tick in ax1.xaxis.get_major_ticks(): tick.label.set_fontsize(16)
for tick in ax1.yaxis.get_major_ticks(): tick.label.set_fontsize(16)

ax1.annotate("Increasing source temp (C)", xy=(1.91, 0.015), xytext=(0.0, 0.03), 
             arrowprops = dict(arrowstyle = "->"), fontsize = 16)

ax1.set_ylabel('Change in fraction of moisture remaining', fontsize = 18, labelpad = 2.0)
ax1.set_xlabel('Change in regional temp (C)', fontsize = 18, labelpad = 1.2)

ax1.set_title('MIS5c/5d change in fraction of moisture remaining with modern Pacific/GoM distribution', fontsize = 20)

plt.savefig('Fraction_model_interglacial', dpi = 100)