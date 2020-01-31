#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:45:30 2019

@author: Chris
"""
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
    plt.xlabel('Distancia hipocentral Km')
    plt.ylabel('Intensidad MMI')
    return model, B0, B1

def int1(logpga):
    '''
    Esta funcion retorna el valor de la intensidad sismica de una estacion 
    como argumento exige el logaritmo del pga de cada estacion para condicion
    de tint 1
    '''
    return abs(2.270 + 1.647*(logpga))

def int2(logpga):
    '''
    Esta funcion retorna el valor de la intensidad sismica de una estacion 
    como argumento exige el logaritmo del pga de cada estacion para condicion
    de tint 2
    '''
    return abs(-1.361 + 3.822*(logpga))

path = '/Users/rt/Desktop/2020-01-17-0429/2020/017/'
canales = list(os.listdir(path))
estaciones = []
c = []
for l in canales:
    if 'HNZ' in l:
        pass
    elif 'ASEGG' in l:
        pass
    elif 'CIRS' in l:
        pass
    elif 'CPREP' in l:
        pass
    else:
        c.append(l)
canales = c
        
def butter_highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = signal.filtfilt(b, a, data)
    return y

def butter_highpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

for i in canales:
    a = i[:i.index('.')]
    estaciones.append(a)




estaciones = list(set(estaciones))
pga = []
for i in estaciones:
    h = len(i)
    chanpga = []
    for j in canales:
        if i == j[:h]:
            x = read(path + j)
            ace = x[0].data
            acel = []
            for k in ace:
                ac = k * 2365.26382 * pow(10, - 7)
                acel.append(ac)
            acef = butter_highpass_filter(acel, 0.5, 100)
            chanpga.append(max(abs(acef)))
    pgaest = np.sqrt(chanpga[0] * chanpga[1])   
    pga.append((i, pgaest))

intensidad = []

for i in pga:
    g = np.log10(i[1])
    if g < 4.87 or g == 4.87:
        intensidad.append(((i[0]),i[1],int1(g)))
    else:
        intensidad.append(((i[0]),i[1],int2(g)))

mapa_set = []

for i in intensidad:
    esta = estacion(i[0])
    if i[2] < 2:
        color = 'white'
    elif i[2] < 3:
        color = '#C7D1F7'
    elif i[2] < 4:
        color = '#81F9EF'
    elif i[2] < 5:
        color = '#73FF9C'
    elif i[2] < 6:
        color = '#F2FA40'
    elif i[2] < 7:
        color = '#FABA00'
    elif i[2] < 8:
        color = '#FD6A02'
    elif i[2] < 9:
        color = '#FF0C03'
    elif i[2] < 10:
        color = '#C4090D'
        
        
    mapa_set.append((i[0], i[1], i[2], esta.latitud, esta.longitud, int(3*i[2]) + 1, color))

print(mapa_set)


path2 = path[:34]

lis = os.listdir(path2)

for i in lis:
    if 'origin' in i:
        t = i
    else:
        pass
    
origin = []

with open(path2 + t, 'r') as f: 
    for i in f:
        origin.append(i) 
ori = []

for i in origin:
    if '9999' in i:
        pass
    else:
        ori.append(i)

p = []
lats = float(ori[0][2:9])
lons = float(ori[0][11:19])
prof = float(ori[0][22:29])
for i in mapa_set:
    dist = distancia2(lats, lons,i[3],i[4])
    dis = np.sqrt(dist**2 + prof**2)
    p.append((i[0], i[1], i[2], i[3], i[4], i[5], i[6], dis))

mapa_set = p

x = []
y =[]




for i in p:
    x.append(i[7])
    y.append(i[2])

parame = reglin(x,y)


##############################################################









import folium
def dibujar_lineas_guia(mi_mapa):
    #LATITUDES
    linea1 = [[13,-95],[13,-87]]
    linea2 = [[14,-95],[14,-87]]
    linea3 = [[15,-95],[15,-87]]
    linea4 = [[16,-95],[16,-87]]
    linea5 = [[17,-95],[17,-87]]
    linea6 = [[18,-95],[18,-87]]
    linea7 = [[19,-95],[19,-87]]
    
    #LONGITUDES
    linea8 = [[13,-95],[19,-95]]
    linea9 = [[13,-94],[19,-94]]
    linea10 = [[13,-93],[19,-93]]
    linea11 = [[13,-92],[19,-92]]
    linea12 = [[13,-91],[19,-91]]
    linea13 = [[13,-90],[19,-90]]
    linea14 = [[13,-89],[19,-89]]
    linea15 = [[13,-88],[19,-88]]
    linea16 = [[13,-87],[19,-87]]
    
    my_PolyLine1=folium.PolyLine(locations=linea1,weight=1,color="gray")
    my_PolyLine2=folium.PolyLine(locations=linea2,weight=1,color="gray")
    my_PolyLine3=folium.PolyLine(locations=linea3,weight=1,color="gray")
    my_PolyLine4=folium.PolyLine(locations=linea4,weight=1,color="gray")
    my_PolyLine5=folium.PolyLine(locations=linea5,weight=1,color="gray")
    my_PolyLine6=folium.PolyLine(locations=linea6,weight=1,color="gray")
    my_PolyLine7=folium.PolyLine(locations=linea7,weight=1,color="gray")
    my_PolyLine8=folium.PolyLine(locations=linea8,weight=1,color="gray")
    my_PolyLine9=folium.PolyLine(locations=linea9,weight=1,color="gray")
    my_PolyLine10=folium.PolyLine(locations=linea10,weight=1,color="gray")
    my_PolyLine11=folium.PolyLine(locations=linea11,weight=1,color="gray")
    my_PolyLine12=folium.PolyLine(locations=linea12,weight=1,color="gray")
    my_PolyLine13=folium.PolyLine(locations=linea13,weight=1,color="gray")
    my_PolyLine14=folium.PolyLine(locations=linea14,weight=1,color="gray")
    my_PolyLine15=folium.PolyLine(locations=linea15,weight=1,color="gray")
    my_PolyLine16=folium.PolyLine(locations=linea16,weight=1,color="gray")
    
    mi_mapa.add_child(my_PolyLine1)
    mi_mapa.add_child(my_PolyLine2)
    mi_mapa.add_child(my_PolyLine3)
    mi_mapa.add_child(my_PolyLine4)
    mi_mapa.add_child(my_PolyLine5)
    mi_mapa.add_child(my_PolyLine6)
    mi_mapa.add_child(my_PolyLine7)
    mi_mapa.add_child(my_PolyLine8)
    mi_mapa.add_child(my_PolyLine9)
    mi_mapa.add_child(my_PolyLine10)
    mi_mapa.add_child(my_PolyLine11)
    mi_mapa.add_child(my_PolyLine12)
    mi_mapa.add_child(my_PolyLine13)
    mi_mapa.add_child(my_PolyLine14)
    mi_mapa.add_child(my_PolyLine15)
    mi_mapa.add_child(my_PolyLine16)

if parame[1] < 2:
    color1 = 'white'
elif parame[1] < 3:
    color1 = '#BE93D4'
elif parame[1] < 4:
   color1 = '#81F9EF'
elif parame[1] < 5:
    color1 = '#73FF9C'
elif parame[1] < 6:
    color1 = '#F2FA40'
elif parame[1] < 7:
    color1 = '#FABA00'
elif parame[1] < 8:
   color1 = '#FD6A02'
elif parame[1] < 9:
   color1 = '#FF0C03'
elif parame[1] < 10:
   color1 = '#C4090D'

m = folium.Map(
    location=[14.4837, -90.6165],
    zoom_start=6,
    tiles='Stamen Terrain'
)

tooltip = 'Estaciones'


for i in mapa_set:
    folium.RegularPolygonMarker([i[3], i[4]],radius=i[5],popup=str(i[2]), tooltip= i[0], fill_color= i[6],).add_to(m)

folium.RegularPolygonMarker([lats, lons],radius = 10,popup=str(parame[1]), tooltip= 'epicentro', fill_color= color1, number_of_sides=8).add_to(m)
    


folium.LayerControl().add_to(m)

dibujar_lineas_guia(m)
m.save("EstacionesTGIF3.html")


#####################################################



I = range(0,int(parame[1]+1))
j = []
di = []
for i in I:
    i = float(i)
    d1 = (1/parame[2])*i - (parame[1]/parame[2])
    di.append(d1)
d = []
for i in di:
    i = i * 0.806416129
    d.append(i)

colorint = []

for i in I:
    if i < 2:
        colo = 'white'
    elif i < 3:
        colo = '#BE93D4'
    elif i < 4:
        colo = '#81F9EF'
    elif i < 5:
        colo = '#73FF9C'
    elif i < 6:
        colo = '#F2FA40'
    elif i < 7:
        colo = '#FABA00'
    elif i < 8:
        colo = '#FD6A02'
    elif i < 9:
       colo = '#FF0C03'
    elif i < 10:
       colo = '#C4090D'
    colorint.append(colo)



if parame[1] < 2:
    color1 = 'white'
elif parame[1] < 3:
    color1 = '#BE93D4'
elif parame[1] < 4:
   color1 = '#81F9EF'
elif parame[1] < 5:
    color1 = '#73FF9C'
elif parame[1] < 6:
    color1 = '#F2FA40'
elif parame[1] < 7:
    color1 = '#FABA00'
elif parame[1] < 8:
   color1 = '#FD6A02'
elif parame[1] < 9:
   color1 = '#FF0C03'
elif parame[1] < 10:
   color1 = '#C4090D'

ma = folium.Map(
    location=[lats, lons],
    zoom_start=7,
    tiles='Stamen Terrain',
    control_scale = True
)

tooltip = 'Mapa de intensidad'

d.remove(d[0])
colorint.remove(colorint[0])
for i in range(len(d)):
    if colorint[i] == 'white':
        u = 0.2
    else:
        u = 0.5
    ma.add_child(folium.CircleMarker([lats,lons], radius = (float(d[i])), color = False, fill_color= colorint[i], fill_opacity = u))

folium.RegularPolygonMarker([lats, lons],radius = 10,popup=str(parame[1]), tooltip= 'epicentro', fill_color= color1, number_of_sides=8).add_to(ma)

#ma.add_child(folium.CircleMarker([lats,lons], radius = 5, color = 'black'))

folium.LayerControl().add_to(ma)

dibujar_lineas_guia(ma)
ma.save("calor.html")
os.system("open calor.html")

with open('intensidad.csv', 'w') as f:
    f.writelines(('{},{},{},{},{},distancia\n').format('Nombre', 'PGA', 'Intensidad', 'lat', 'lon'))
    for i in mapa_set:
        f.writelines(('{},{},{},{},{},{}\n').format(i[0],str(i[1]),str(i[2]),str(i[3]),str(i[4]),str(i[7])))
    f.writelines('{},{},{},{},{},{}'.format('epicentro','n/a',parame[1],lats,lons,'n/a',''))