#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 16:12:57 2020

@author: rt
"""
import pandas as pd
import os 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from mpl_toolkits.mplot3d import  axes3d
from matplotlib import style, cm
import statsmodels.formula.api as smf
db = pd.read_csv('anual.csv')


def reglin(x,y):
    x =  sm.add_constant(x)
    model = sm.OLS(y,x).fit()
    B0 = model.params[0]
    B1 = model.params[1]
    x = x[:, 1]
    x2 = np.linspace(x.min(), x.max(), 100)
    y_hat = x2 * B1 + B0
    plt.scatter(x,y,alpha = 1)
    plt.plot(x2, y_hat, 'r', alpha = 1)
    plt.xlabel('Magnitud Local')
    plt.ylabel('log(Frecuencia acumulada de sismos)')
    plt.title("Ley de Gutenberg-Richter")
    plt.legend(['Pendiente = {}, Corte = {}'.format(round(B1, 2), round(B0,2))])
    return model, B0, B1


#######histograma de magnitud ley de richter########
#plt.hist(db[' Magnitud'], bins = 20)
#plt.xlabel('Magnitud Local')
#plt.ylabel('Cuenta')
#plt.title('Histograma de Magnitud')
#plt.vlines(3.58,0,153, colors = 'r', label = 'Magnitud Minima = 3.58')
#plt.legend()
#plt.show()
##############################################
#plt.hist(db[' Profundidad'], bins = 24)
#plt.xlabel('Profundidad (Km)')
#plt.ylabel('Cuenta')
#plt.title('Histograma de Profundidad')
#plt.show()
############################################# 
x = db[' Tiempo de origen (UTC)']
x = list(x)
mes = []
for i in x:
    mes.append(i[5:7])
#plt.hist(mes, bins = 12)
#plt.xlabel('No. de mes')
#plt.ylabel('Cuenta')
#plt.title('Histograma de sismos por mes')
##########################################
#plt.scatter(db['No.'], db[' Magnitud'])
#plt.xlabel('Sismos ordenados por tiempo de origen')
#plt.ylabel('Magnitud Local')
#plt.title('Magnitud en serie de tiempo')
###########################################
#plt.scatter(mes, db[' Magnitud'])
#plt.xlabel('No. de mes')
#plt.ylabel('Magnitud Local')
#plt.title('Magnitud por Mes')
##############################################
hist,bins = np.histogram(db[' Magnitud'], bins = 20)
histlog = np.log10(hist[9:])
hh = hist[9:]
bins = bins[10:]
#a,b,c = reglin(bins, histlog)
###########################################gr
#acu =[]
#for i in range(len(histlog)):
#    acu.append(sum(hh[i:]))
#acu = np.log10(acu)
#a,b,c = reglin(bins, acu)

###########################################
#fig = plt.figure()
#ax1 = fig.add_subplot(1,1,1, projection = '3d')
#m = ax1.scatter(db[' Latitud'], db[' Longitud'], - db[' Profundidad'], c = - db[' Profundidad'])
#fig.colorbar(m, shrink=0.5, aspect=10, label = 'Profundidad Km')
##ax1.set_clim(min(- db[' Profundidad']), max(- db[' Profundidad']))
#plt.xlabel('Latitud °')
#plt.ylabel('Longitud °')
#ax1.set_zlim(min( - db[' Profundidad'])),  max(- db[' Profundidad'])
#plt.title('Ploteo de sismos en coordenadas espaciales')
#plt.show()






#############################################
#plt.scatter(mes, db[' Latitud'])
#plt.xlabel('No. de mes')
#plt.ylabel('Latitud °')
#plt.title('Latitud por Mes')
##############################################

#mm = []
#for i in mes:
#    mm.append(int(i))
#hist,bins = np.histogram(mm, bins = 12)
#    
#fig, ax = plt.subplots()
#c =db[' Magnitud']
#im = ax.scatter(mm, c,  s = 20, c = c)
#fig.colorbar(im, ticks=[min(c), max(c)], label = 'Magnitud Local')
#im.set_clim(min(c), max(c))
#plt.xlabel('Tiempo por mes')
#plt.ylabel('Magnitud Local')
#plt.title('Sismisidad Recurrente')
###################################################

#lat = []
#lon = []
#prof = []
#todo = []
#for i in range(len(db[' Latitud'])):
#    todo.append((db[' Latitud'][i], db[' Longitud'][i], db[' Profundidad'][i]))
#for i in todo:
#    if i[0] < 15 and i[2] > 74:
#        lat.append(i[0])
#        lon.append(i[1])
#        prof.append(i[2])
#with open('mult.csv', 'w') as f:
#    f.write('lat,lon,prof,hola' + '/n')
#    for i in range(len(lat)):
#        f.write(str(lat[i]) + ',' + str(lon[i]) + ',' + str(prof[i]) + '\n')


#sub = pd.read_csv('mult.csv')
#model = smf.ols(formula='prof~lat+lon', data=sub)
#model_fit = model.fit()
#
#
#fig = plt.figure(figsize=(12, 9))
#ax = axes3d.Axes3D(fig)
#ax.scatter(sub.lat, sub.lon, sub.prof)
#
#xs = np.linspace(*ax.get_xlim(), 100)
#ys = np.linspace(*ax.get_ylim(), 100)
#xv, yv = np.meshgrid(xs, ys, copy=False)
#zv = np.zeros((ys.size, xs.size))
#lv = np.zeros((ys.size, xs.size))
#uv = np.zeros((ys.size, xs.size))
#
#for idx, y in enumerate(yv):
#    pred = model_fit.get_prediction({'lat': xs, 'lon': y}).summary_frame()
#    zv[idx] = pred['mean']
#    lv[idx] = pred['mean_ci_lower']
#    uv[idx] = pred['mean_ci_upper']
#
#ax.plot_surface(xv, yv, zv, alpha=0.4)
##ax.plot_surface(xv, yv, lv, alpha=0.2, color='C1')
##ax.plot_surface(xv, yv, uv, alpha=0.2, color='C1')
#
#ax.contourf(xv, yv, uv-lv,
#            zdir='z',
#            offset=ax.get_zlim()[0],
#            levels=30,
#            antialiased=True,
#            alpha=0.4,
#            cmap=cm.Oranges)
#
#ax.set_title('Linear regression on Boston housing data: medv ~ lstat + age')
#ax.set_xlabel('lat')
#ax.set_ylabel('lon')
#ax.set_zlabel('prof')










#ax1 = fig.add_subplot(111, projection = '3d')
#ax1.scatter(lat, lon, prfo)
#plt.xlabel('Latitud °')
#plt.ylabel('Longitud °')
#plt.title('Ploteo de sismos en coordenadas espaciales')
#plt.show()
################################################################
#a = db[(db[" Latitud"] <= 14.954) & (db[" Latitud"] >= 14.180) & (db[" Longitud"] <= -90.186) & (db[" Longitud"] >= -90.818)]
#
#
#
#
#plt.hist(a[' Magnitud'], bins = 20)
#plt.xlabel('Magnitud Local')
#plt.ylabel('Cuenta')
#plt.title('Histograma de Magnitud')
#plt.vlines(2.4,0,21.92, colors = 'r', label = 'Magnitud Minima = 2.4')
#plt.legend()
#plt.show()
#hist,bins = np.histogram(a[' Magnitud'], bins = 20)
#histlog = np.log10(hist[9:])
#hh = hist[8:]
#bins = bins[9:]
#
#acu =[]
#for i in range(len(hh)):
#    acu.append(sum(hh[i:]))
#acu = np.log10(acu)
#a,b,c = reglin(bins, acu)
################################################################
sup = 0
inter = 0
pro = 0
for i in db[' Profundidad']:
    if i < 25:
        sup = sup +1
    elif i >= 25 and i < 70:
        inter = inter +1
    else:
        pro = pro + 1

labels = ['Superficiales','Intermedios', 'Profundos']
sizes = [sup, inter, pro]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Distribucion de sismos por Profundidad')
plt.show()
























