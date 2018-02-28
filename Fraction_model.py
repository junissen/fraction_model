#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 11:19:22 2018

@author: julianissen
"""

import numpy as np

class localTempChange():
    
    def __init__(self, sourceTemp, d_source, startL, endC, RH, ax, xlim, ylim, color): 
        
        self.sourceTempC = sourceTemp
        self.RH = RH
        self.ax = ax
        self.x_lim = xlim
        self.y_lim = ylim
        self.startL= startL
        self.endC = endC
        self.d_source = d_source
        self.color = color
        self.startL = startL
        self.endC = endC
        
        self.Tstart = 8.3
        
        #Constants for dew point temp calculation
        self.Lambda = 243.12 #in C
        self.Beta = 17.62
        
        #Output arrays
        self.diffTemp_array = []
        self.F_array = []
        
    
    def F_function_LGM(self):
        
        T_org = self.Tstart
        modern_source_temp = 25.13 + 273.15
        ax = self.ax
        T = self.Tstart
        Tsource = self.sourceTempC + 273.15
        dT = 0.1
        diff = 0
        
        while diff > -13.0:
            
            T_k = T + 273.15
        
            #Fraction at modern
            alpha_evap_mod = np.exp((1.137*((10**3)/(modern_source_temp**2))) - (0.4156/modern_source_temp) - (2.0667*(10**-3))) #from Majoube 1971
            dv_i_mod = self.d_source - ((10**3)*np.log10(alpha_evap_mod)) #from Rohling 2013
            
            dDewPointC_mod = (self.Lambda * (np.log(self.RH/100.0) + ((self.Beta * T_org)/(self.Lambda + T_org))))/(self.Beta - (np.log(self.RH/100.0) + ((self.Beta * T_org)/(self.Lambda + T_org))))
            dDewPointK_mod = dDewPointC_mod + 273.15
            
            alpha_precip_mod = np.exp((-7.685 + 6.7123*((10**3)/dDewPointK_mod) - 1.6664*((10**6)/(dDewPointK_mod**2)) #from Dansgaard 1964, assuming constant alpha
                            + 0.35041*((10**9)/(dDewPointK_mod**3)))/1000)
            
            V_mod = ((self.startL + 1000)/alpha_precip_mod) - 1000
            F_mod = np.exp((np.log(V_mod + 1000) - np.log(dv_i_mod + 1000))/(((alpha_evap_mod + alpha_precip_mod)/2) - 1))
            
            #Fraction at LGM 
            alpha_evap_LGM = np.exp((1.137*((10**3)/(Tsource**2))) - (0.4156/Tsource) - (2.0667*(10**-3))) #from Majoube 1971
            dv_i_LGM = self.d_source - ((10**3)*np.log10(alpha_evap_LGM)) #from Rohling 2013
            
            dDewPointC_LGM = (self.Lambda * (np.log(self.RH/100.0) + ((self.Beta * T)/(self.Lambda + T))))/(self.Beta - (np.log(self.RH/100.0) + ((self.Beta * T)/(self.Lambda + T))))
            dDewPointK_LGM = dDewPointC_LGM + 273.15
            
            alpha_precip_LGM = np.exp((-7.685 + 6.7123*((10**3)/dDewPointK_LGM) - 1.6664*((10**6)/(dDewPointK_LGM**2)) #from Dansgaard 1964, assuming constant alpha
                            + 0.35041*((10**9)/(dDewPointK_LGM**3)))/1000)
            
            
            dC_VSMOW = (1.03019 * self.endC) + 30.91
            dL_LGM = np.exp(((((10**3) * np.log(dC_VSMOW + 1000)) - (2.78 * (10**6)/(T_k**2)) + 2.89)/1000)) - 1000
            
            V_LGM = ((dL_LGM + 1000)/alpha_precip_LGM) - 1000
            F_LGM = np.exp((np.log(V_LGM + 1000) - np.log(dv_i_LGM + 1000))/(((alpha_evap_LGM + alpha_precip_LGM)/2) - 1))
            
            
            #Difference in F
            F = F_LGM - F_mod
            
            self.diffTemp_array.append(diff)
            self.F_array.append(F)
            
            if (2.2 <= T <= 2.3):
                print "at 2.3temp fraction of moisture remaining is " + str(F_LGM) + "and difference in F is " + str(F)
                
            
            T = T - dT
            diff = T - self.Tstart

        ax.set_xlim(self.x_lim)
        ax.set_ylim(self.y_lim)
        fraction = ax.plot(self.diffTemp_array, self.F_array, self.color, linewidth = 1)
        return fraction
    
    def F_function_interglacial(self):
        
        T_org = self.Tstart
        modern_source_temp = 25.13 + 273.15
        ax = self.ax
        T = self.Tstart
        Tsource = self.sourceTempC + 273.15
        dT = 0.1
        diff = 0
        
        while diff < 13.0:
            
            T_k = T + 273.15
        
            #Fraction at modern
            alpha_evap_mod = np.exp((1.137*((10**3)/(modern_source_temp**2))) - (0.4156/modern_source_temp) - (2.0667*(10**-3))) #from Majoube 1971
            dv_i_mod = self.d_source - ((10**3)*np.log10(alpha_evap_mod)) #from Rohling 2013
            
            dDewPointC_mod = (self.Lambda * (np.log(self.RH/100.0) + ((self.Beta * T_org)/(self.Lambda + T_org))))/(self.Beta - (np.log(self.RH/100.0) + ((self.Beta * T_org)/(self.Lambda + T_org))))
            dDewPointK_mod = dDewPointC_mod + 273.15
            
            alpha_precip_mod = np.exp((-7.685 + 6.7123*((10**3)/dDewPointK_mod) - 1.6664*((10**6)/(dDewPointK_mod**2)) #from Dansgaard 1964, assuming constant alpha
                            + 0.35041*((10**9)/(dDewPointK_mod**3)))/1000)
            
            V_mod = ((self.startL + 1000)/alpha_precip_mod) - 1000
            F_mod = np.exp((np.log(V_mod + 1000) - np.log(dv_i_mod + 1000))/(((alpha_evap_mod + alpha_precip_mod)/2) - 1))
            
            #Fraction at interglacial
            alpha_evap_interglacial = np.exp((1.137*((10**3)/(Tsource**2))) - (0.4156/Tsource) - (2.0667*(10**-3))) #from Majoube 1971
            dv_i_interglacial = self.d_source - ((10**3)*np.log10(alpha_evap_interglacial)) #from Rohling 2013
            
            dDewPointC_interglacial = (self.Lambda * (np.log(self.RH/100.0) + ((self.Beta * T)/(self.Lambda + T))))/(self.Beta - (np.log(self.RH/100.0) + ((self.Beta * T)/(self.Lambda + T))))
            dDewPointK_interglacial = dDewPointC_interglacial + 273.15
            
            alpha_precip_interglacial = np.exp((-7.685 + 6.7123*((10**3)/dDewPointK_interglacial) - 1.6664*((10**6)/(dDewPointK_interglacial**2)) #from Dansgaard 1964, assuming constant alpha
                            + 0.35041*((10**9)/(dDewPointK_interglacial**3)))/1000)
            
            
            dC_VSMOW = (1.03019 * self.endC) + 30.91
            dL_interglacial = np.exp(((((10**3) * np.log(dC_VSMOW + 1000)) - (2.78 * (10**6)/(T_k**2)) + 2.89)/1000)) - 1000
            
            V_interglacial = ((dL_interglacial + 1000)/alpha_precip_interglacial) - 1000
            F_interglacial = np.exp((np.log(V_interglacial + 1000) - np.log(dv_i_interglacial + 1000))/(((alpha_evap_interglacial + alpha_precip_interglacial)/2) - 1))
            
            
            #Difference in F
            F = F_interglacial - F_mod
            
            self.diffTemp_array.append(diff)
            self.F_array.append(F)
            
            
            T = T + dT
            diff = T - self.Tstart

        ax.set_xlim(self.x_lim)
        ax.set_ylim(self.y_lim)
        fraction = ax.plot(self.diffTemp_array, self.F_array, self.color, linewidth = 1)
        return fraction
    
    def F_fraction_l(self, Tend):
        
        Tsource = self.sourceTempC + 273.15
        Tend = Tend
        dl = self.startL
        
        alpha_evap = np.exp((1.137*((10**3)/(Tsource**2))) - (0.4156/Tsource) - (2.0667*(10**-3))) #from Majoube 1971
        dv_i = self.d_source - ((10**3)*np.log10(alpha_evap))
        
        dDewPointC = (self.Lambda * (np.log(self.RH/100.0) + ((self.Beta * Tend)/(self.Lambda + Tend))))/(self.Beta - (np.log(self.RH/100.0) + ((self.Beta * Tend)/(self.Lambda + Tend))))
        dDewPointK = dDewPointC + 273.15
        
        alpha_precip = np.exp((-7.685 + 6.7123*((10**3)/dDewPointK) - 1.6664*((10**6)/(dDewPointK**2)) #from Dansgaard 1964, assuming constant alpha
                            + 0.35041*((10**9)/(dDewPointK**3)))/1000)
        dv = ((dl + 1000)/alpha_precip) - 1000
        F = np.exp((np.log(dv + 1000) - np.log(dv_i + 1000))/(((alpha_evap + alpha_precip)/2) - 1))
        
        print "For " + str(Tend) + "end temp and dl of " + str(dl) + ": " + str(F) + " fraction of moisture remaining"
    
    def F_fraction_c(self, Tend):
        print "For " + str(Tend) + "end temp and dc of " + str(self.endC)
        
        Tsource = self.sourceTempC + 273.15
        Tend = Tend
        dc = self.endC
        T_k = Tend + 273.15
        
        alpha_evap = np.exp((1.137*((10**3)/(Tsource**2))) - (0.4156/Tsource) - (2.0667*(10**-3))) #from Majoube 1971
        dv_i = self.d_source - ((10**3)*np.log10(alpha_evap))
        
        dDewPointC = (self.Lambda * (np.log(self.RH/100.0) + ((self.Beta * Tend)/(self.Lambda + Tend))))/(self.Beta - (np.log(self.RH/100.0) + ((self.Beta * Tend)/(self.Lambda + Tend))))
        dDewPointK = dDewPointC + 273.15
        
        alpha_precip = np.exp((-7.685 + 6.7123*((10**3)/dDewPointK) - 1.6664*((10**6)/(dDewPointK**2)) #from Dansgaard 1964, assuming constant alpha
                            + 0.35041*((10**9)/(dDewPointK**3)))/1000)
        print "alpha precip: " + str(alpha_precip)
        dC_VSMOW = (1.03019 * dc) + 30.91
        dL = np.exp(((((10**3) * np.log(dC_VSMOW + 1000)) - (2.78 * (10**6)/(T_k**2)) + 2.89)/1000)) - 1000
        alpha_calc = np.exp(((2.78 * (10**6)/(T_k**2)) + 2.89)/1000)
        print "alpha calcite: " + str(alpha_calc)
        print "dL calculated: " + str(dL)
        
        dv = ((dL + 1000)/alpha_precip) - 1000
        print "dv calculated: " + str(dv)
        F = np.exp((np.log(dv + 1000) - np.log(dv_i + 1000))/(((alpha_evap + alpha_precip)/2) - 1))
            
        print str(F) + " fraction of moisture remaining"
        print "--------------------"
        
        