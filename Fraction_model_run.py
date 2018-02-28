#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 12:05:31 2018

@author: julianissen
"""

import Fraction_model_temp as temp_model
import Fraction_model as frac_model
import matplotlib.pyplot as plt
import numpy as np

fig1 = plt.figure(figsize = (14, 14))
ax1 = fig1.add_subplot(1,1,1)

fig2 = plt.figure(figsize = (14,14))
ax2 = fig2.add_subplot(1,1,1)

x1_lim = [0.5, -14]
y1_lim = [-0.04, 0.062]

x2_lim = [0.5, -14]
y2_lim = [-0.025, 0.073]

model1 = temp_model.sourceTempChange(25.13, 1.25, -7.24, -3.7, 68, ax1, x1_lim, y1_lim)
model1.T_function_LGM()

model2 = temp_model.sourceTempChange(25.13, 1.25, -7.92, -3.7, 68, ax2, x2_lim, y2_lim)
model2.T_function_LGM()

modelModern = frac_model.localTempChange(25.13, 1.25, -7.92, -3.7, 68, ax2, x2_lim, y2_lim, "none")
modelModern.F_fraction_l(8.3)

modelModern2 = frac_model.localTempChange(25.13, 1.25, -7.24, -3.7, 68, ax2, x2_lim, y2_lim, "none")
modelModern2.F_fraction_l(8.3)

modelLGM = frac_model.localTempChange(25.13, 1.25, -7.92, -3.7, 68, ax2, x2_lim, y2_lim, "none")
modelLGM.F_fraction_c(8.3)

modelmodern_alt = frac_model.localTempChange(25.13, 1.25, -9.2, -5.78, 68, ax2, x2_lim, y2_lim, "none");
modelmodern_alt.F_fraction_c(8.3)

modelLGM = frac_model.localTempChange(25.13, 1.25, -7.92, -3.7, 68, ax2, x2_lim, y2_lim, "none")
modelLGM.F_fraction_c(2.4) #with 5.9degree decrease 

modelLGM2 = frac_model.localTempChange(22.63, 1.25, -7.92, -3.7, 68, ax2, x2_lim, y2_lim, "none")
modelLGM2.F_fraction_c(2.4) #with 5.9degree decrease 

modelLGM3 = frac_model.localTempChange(20.13, 1.25, -7.92, -3.7, 68, ax2, x2_lim, y2_lim, "none")
modelLGM3.F_fraction_c(2.4) #with 5.9degree decrease 


modelLGM = frac_model.localTempChange(25.13, 1.25, -7.92, -3.7, 68, ax2, x2_lim, y2_lim, "none")
modelLGM.F_fraction_c(-3.7) #with 12degree decrease

modelLastInterglacial = frac_model.localTempChange(25.13, 1.25, -7.92, -7.87, 68, ax2, x2_lim, y2_lim, "none")
modelLastInterglacial.F_fraction_c(8.3) #with same temp
modelLastInterglacial.F_fraction_c(10.3) #with 2degree increase
modelLastInterglacial.F_fraction_c(12.3) #with 4degree increase

y1_major_ticks = np.arange(-0.04, 0.062, 0.02)
y1_minor_ticks = np.arange(-0.04, 0.062, 0.01)
x1_major_ticks = np.arange(-13, 0, 2)
x1_minor_ticks = np.arange(-13, 0, 1)

y2_major_ticks = np.arange(-0.02, 0.073, 0.02)
y2_minor_ticks = np.arange(-0.02, 0.073, 0.01)
x2_major_ticks = np.arange(-13, 0, 2)
x2_minor_ticks = np.arange(-13, 0, 1)


ax1.set_yticks(y1_major_ticks)
ax1.set_yticks(y1_minor_ticks, minor=True)
ax1.set_xticks(x1_major_ticks)
ax1.set_xticks(x1_minor_ticks, minor=True)

ax2.set_yticks(y2_major_ticks)
ax2.set_yticks(y2_minor_ticks, minor=True)
ax2.set_xticks(x2_major_ticks)
ax2.set_xticks(x2_minor_ticks, minor=True)

for tick in ax1.xaxis.get_major_ticks(): tick.label.set_fontsize(16)
for tick in ax1.yaxis.get_major_ticks(): tick.label.set_fontsize(16)

for tick in ax2.xaxis.get_major_ticks(): tick.label.set_fontsize(16)
for tick in ax2.yaxis.get_major_ticks(): tick.label.set_fontsize(16)

ax1.annotate("Decreasing source temp (C)", xy=(-1.85, -0.003), xytext=(0.2, -0.035), 
             arrowprops = dict(arrowstyle = "->"), fontsize = 16)

ax2.annotate("Decreasing source temp (C)", xy=(-1.85, 0.01), xytext=(0.2, -0.02), 
             arrowprops = dict(arrowstyle = "->"), fontsize = 16)  

ax1.set_ylabel('Change in fraction of moisture remaining', fontsize = 18, labelpad = 2.0)
ax1.set_xlabel('Change in regional temp (C)', fontsize = 18, labelpad = 1.2)

ax2.set_ylabel('Change in fraction of moisture remaining', fontsize = 18, labelpad = 2.0)
ax2.set_xlabel('Change in regional temp (C)', fontsize = 18, labelpad = 1.2)

d18o = r'$\delta^{18}\!O$'

permille = u"\u2030"

ax1.set_title('MIS2/3 change in fraction of moisture remaining with Pacific moisture eliminated', fontsize = 20)
ax2.set_title('MIS2/3 change in fraction of moisture remaining with modern Pacific/GoM distribution', fontsize = 20)

#fig.tight_layout()

#plt.subplots_adjust(bottom=-0.2)

#fig1.savefig("Fraction_model_LGM1", dpi = 100)
#fig2.savefig("Fraction_model_LGM2", dpi = 100)
