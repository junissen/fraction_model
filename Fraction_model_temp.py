#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 12:50:31 2018

@author: julianissen
"""

import Fraction_model as fraction_model

class sourceTempChange():
    
    def __init__ (self, startTemp, dsource, startL, endL, RH, ax, xlim, ylim):
        
        self.startTemp = startTemp
        self.dsource = dsource
        self.RH = RH
        self.ax = ax
        self.xlim = xlim
        self.ylim = ylim
        self.dT = 1
        self.startL = startL
        self.endL = endL

        
    def T_function_LGM(self):
        
        color_array = ['darkblue', 'slateblue', 'rebeccapurple', 'darkviolet', 'violet', 'fuchsia', 'deeppink', 'crimson']
        counter = 0
        T = self.startTemp
        
        while counter < 8:
            
            local_color = color_array[counter]
            model = fraction_model.localTempChange(T, self.dsource, self.startL, self.endL, self.RH, self.ax, self.xlim, self.ylim, local_color)
            model.F_function_LGM()

            counter = counter + 1
            T = T - self.dT
        
    def T_function_interglacial(self):
        
        color_array = ['darkblue', 'slateblue', 'rebeccapurple', 'darkviolet', 'violet', 'fuchsia', 'deeppink', 'crimson']
        counter = 7
        T = self.startTemp
        
        while counter >= 0:
            
            local_color = color_array[counter]
            model = fraction_model.localTempChange(T, self.dsource, self.startL, self.endL, self.RH, self.ax, self.xlim, self.ylim, local_color)
            model.F_function_interglacial()

            counter = counter - 1
            T = T + self.dT
            
            
            
            
        