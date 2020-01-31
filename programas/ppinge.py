#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 14:13:58 2020

@author: Christian Ramirez
"""
#####################Modulos usados############################
from obspy import read
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import os
import sys
from geophysics import estacion ,distancia2
import statsmodels.api as sm
import statsmodels.stats.diagnostic as smd
from scipy.optimize import curve_fit
import subprocess
###############################################################


def butter_highpass_filter(data, cutoff, fs, order=5):# Funcion que permite filtrar la data con un HP
    b, a = butter_highpass(cutoff, fs, order=order)
    y = signal.filtfilt(b, a, data)
    return y

def butter_highpass(cutoff, fs, order=5): # Funcion que calcula constantes para el filtro
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

path = '/Users/rt/Desktop/pp 2.0/crudo/2019-02-01-1613/2019/032/'
canales = list(os.listdir(path))
estaciones = []
c = []
for l in canales:
    if 'TEST' in l:
        pass
    elif 'ASEGG' in l:
        pass
    elif 'CIRS' in l:
        pass
    elif 'CPREP' in l:
        pass
    elif 'Store' in l:
        pass
    else:
        c.append(l)
canales = c

for i in canales: #extraccion y lmacenamiento de data
    crudo = read(path + i)
    aceleracion_sin_calibracion = crudo[0].data
    aceleracion_sin_filtro = []
    for j in aceleracion_sin_calibracion:
        a = j * 2365.26382 * pow(10, - 7)
        aceleracion_sin_filtro.append(a)
    aceleracion = butter_highpass_filter(aceleracion_sin_filtro, 0.5, 100)
    with open('/Users/rt/Desktop/pp 2.0/procesado/2019-02-01-1613/' + i +'.txt', 'w') as f:
        for k in aceleracion:
            f.writelines(str(k) + '\r \n')