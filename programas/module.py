#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 12:46:00 2019

@author: Christian Ramirez & Victor Tzorin
"""
import os
from os import listdir
from numpy import exp
import time
from PIL import Image, ImageDraw, ImageFont
import shutil
import reverse_geocoder as rg
import numpy as np

def loc_sis(coordinates):
    '''
    Esta funcion saca la ciudad mas cercana del sismo y la distancia 
    Ejemplo:      
    >>> loc_sis((14.026194, -91.734658))
    >>> ['San Jose La Maquina', 35.58399650504598, 'Guatemala']
    '''
    
    #Information provided by the user
    evinfo = rg.search(coordinates, mode = 2)
    
    #Conversion factor
    radian = np.pi / 180
    
    #Geographic and demographic information
    evcity = evinfo[0]['name']
    evcntr = evinfo[0]['cc']
    latcit = float(evinfo[0]['lat']) * radian
    loncit = float(evinfo[0]['lon']) * radian
    evelat = float(coordinates[0]) * radian
    evelon = float(coordinates[1]) * radian
    
    #Calculations
    dislat = latcit - evelat
    dislon = loncit - evelon
    radius = 2.0 * 6372.795477598
    distan = radius * np.arcsin(np.sqrt((np.sin(dislat / 2.0) * (np.sin(dislat / 2.0))) + (np.cos(latcit) * np.cos(evelat) * (np.sin(dislon / 2.0) * (np.sin(dislon / 2.0))))))

    #Substitution of the acronym of the country
    if evcntr == 'GT':
        evcntr = 'Guatemala'
    elif evcntr == 'MX':
        evcntr = 'Mexico'
    elif evcntr == 'SV':
        evcntr = 'El Salvador'
    elif evcntr == 'HN':
        evcntr = 'Honduras'
    elif evcntr == "NI":
        evcntr = 'Nicaragua'
    else:
        evcntr = 'UBICACIÓN NO AGREGADA'
    a = [evcity, distan, evcntr]
    
    return a

def remover(event_name, stations_names):
    """
    La funcion remover recibe event_name que es una varible tipo cadena que
    es el codigo de cada evento y la variable stations_names que es una lista
    de los sensores que se desea borrar. Este programa esta acondicionado para
    un sistema operativo con lenguaje de terminal tipo Bash especialmente para
    el sistema operativo iOS puede funcionar tambien en algunos sistemas de 
    distribución linux
    """

    #Names of the stations that are going to be deleted
    stname = stations_names
    evname = event_name

    drctry = evname[0:4]+'/'+evname[5:7]+'/'+event_name

    #List of all the files in the current directory
    filst1 = os.listdir(drctry)

    #Cycle that analyzes all files in the current directory
    for i in filst1:
        #The program tries to convert the name of the file to a number
        try:
            i=int(i)
        except:
            pass
    
        #If the conversion is successful, then it is the file that we want and we add it to our directory
        if type(i) == int:
            drctry = drctry + "/" + str(i).zfill(4)
            
        else:
            pass

    #List of all the files in the current directory
    filst2 = os.listdir(drctry)

    #Cycle that analyzes all files in the current directory
    for j in filst2:
        #The program tries to convert the name of the file to a number
        try:
            j=int(j)
        except:
            pass
        #If the conversion is successful, then it is the file that we want and we add it to our directory
        if type(j) == int: 
            drctry = drctry + "/" + str(j).zfill(3)
            
        else:
            pass

    #List of all the files in the current directory
    filst3=os.listdir(drctry)

    #Part of the program that deletes stations according to its name
    for k in stname:
    
        #Cycle that analyzes all files in the current directory   
        for i in filst3:
            #Lenght of the name of the station
            first = len(k)
        
            #Comparison between the name of the station and the name of the file. If they are the same, the file is remove
            if i[:first]==k:
                os.remove(drctry + "/" + i)
            
            else:
                pass

    #Cycle that analyzes all files in the first directory   
    for l in filst1:
        #If the desired table is found (wfdisc), its name is store
        if l[-6:] == "wfdisc" and l[0] != "c":
            wf=l
        
        else:
            pass
    
    archivo=[]

    #A modified copy, without the stations that we don't want, is made
    with open(drctry[0:20]+wf, "r") as table1:
        for culine in table1:
            for m in stname:
                clave = len(m)
            
                if m == culine[:clave]:
                    culine = ""
                
                else:
                    pass
            
            archivo.append(culine)
        
        #The table is overwritten
        with open(drctry[0:20]+'/'+wf, "w") as table2:
            table2.writelines(archivo)
  
          
def info_extractor(initial_date,final_date, map_type):
    """
    Saca la informacion en un formato texto, jason y lo pone en un mapa
    """

    #Dates input
    indate = initial_date
    fidate = final_date

    #Directories of images
    mapmun = 'map_files/mapa_mundial.png'
    mapreg = 'map_files/mapa_regional.png'
    leyen1 = 'map_files/leyenda1.png'
    leyen2 = 'map_files/leyenda2.png'

    #Type of map: magnitude, depth, none
    mptype = map_type

    #Variables used in the program
    cuyear = 0
    fiyear = 1

    iniday = int(indate[8:10]) 
    finday = int(fidate[8:10])

    evorid = []
    evnumb = []
    templi = []

    #Variables that store the information
    utctim = []
    loctim = []
    latitu = []
    longit = []
    edepth = []
    residu = []
    usstat = []
    magnit = []
    imagni = []
    region = []
    
    #Cycle that ends until all the years have been analyzed

    while True:
    
        cuyear = cuyear + 1
    
        #Stablishing initial conditions
        if cuyear == 1:
            cuyear = int(indate[0:4])
            fiyear = int(fidate[0:4])
    
        else:
            pass

        #Cycle that ends until all the months have been analyzed

        #Variables used in the program
        cumnth = 0
        fimnth = 1
    
        while True:
        
            cumnth = cumnth + 1
        
    
            #Stablishing initial conditions
            if cumnth == 1:
                cumnth = int(indate[5:7])
                fimnth = int(fidate[5:7])
    
            else:
                pass
    
            #List that contains all the folders of the events of the month that is currently being analyzed
            allday = []
            for i in sorted(listdir(str(cuyear)+'/'+str(cumnth).zfill(2))):
                allday.append(i)
    
            #Cycle that runs through all the folders
            for j in allday:

                try:

                    #Only the events in the desired range of days/weeks/months are analyzed
                    if (int(indate[5:7]) == cumnth and iniday > int(j[8:10])):
                        pass

            
                    elif (fimnth == cumnth and finday < int(j[8:10])):

                        pass
                
                    else:

                        try:
                            #Cycle that enters each folder and analyzes all the files of the event it contains
                            for k in listdir(str(cuyear)+'/'+str(cumnth).zfill(2)+'/'+j):
                                try:
                                    #If the origin file is found, it is open
                                    if k[0:4] == str(cuyear) and k[-6:] == 'origin':
                                        evnumb.append(k[0:8])
                                        cufile = open(str(cuyear)+'/'+str(cumnth).zfill(2)+'/'+j+'/'+k)
                                        #Cycle that runs through the file and extracts the origin time, latitude, longitude, depth and id of the event
                                        for l in cufile:
                                            if l[0] == '-':
                                                pass
                                            else:
                                                try:
                                                    utctim.index(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(l[31:47])+6*3600)))
                                                except:
                                                        utctim.append(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(l[31:47])+6*3600)))
                                                        loctim.append(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(l[31:47]))))
                                                        latitu.append(l[2:9])
                                                        longit.append('-'+l[12:19])
                                                        edepth.append(l[21:29])
                                                        
                                                        evorid.append(l[51:56])
                                    else:
                                        pass
                                        
                                except:
                                    pass

                        except:
                            pass

                    #Cycle that opens the origerr file and extracts the RMS of the solution for the event
                    cufile = open(str(cuyear)+'/'+str(cumnth).zfill(2)+'/'+j+'/'+evnumb[-1]+'.origerr')
            
                    for m in cufile:
                        if int(m[0:8]) == int(evorid[-1]):
                            residu.append(m[172:178])
                
                        else:
                            pass
            
                    #Cycle that opens the assoc file and extracts the amount of stations used to locate the event
                    cufile = open(str(cuyear)+'/'+str(cumnth).zfill(2)+'/'+j+'/'+evnumb[-1]+'.assoc')
            
                    for n in cufile:
                        try:
                            templi.index(n[18:22])
                    
                        except:
                            if n[18:22] != '-   ' and n[12:17] == evorid[-1]:
                                templi.append(n[18:22])
                        
                            else:
                                pass
            
                    usstat.append(str(len(templi)))
                    templi = []
            
                    #Cycle that opens the netmag file and extracts the magnitude of the event and its uncertainty
                    cufile = open(str(cuyear)+'/'+str(cumnth).zfill(2)+'/'+j+'/'+evnumb[-1]+'.netmag')
            
                    for o in cufile:
                        
                        if int(o[18:26]) == int(evorid[-1]):
                            magnit.append(o[55:59])
                            imagni.append(o[63:67])
                            
                        else:
                            pass
        
                except:
                    pass
        
            #Variables that end the cycle that analyzes the months
            if cumnth == 12:
                indate = str(cuyear)+'-01-01'
                break
        
            elif cumnth == fimnth and cuyear == fiyear:
                break
        
            else:
                pass
    
        #Variables that end the cycle that analyzes the years
        if cuyear == fiyear:
            break
    
        else:
            pass

    #Cycle that creates the map with all the locations and magnitudes of the events extracted

    #Original map
    image1 = Image.open(mapreg)
    drawim = ImageDraw.Draw(image1)

    #Latitudes and longitudes of the initial and final points of the map
    lapuin = 18.8613689546248
    lopuin = -94.2427589202773

    lapufi = 12.18602717452006
    lopufi = -87.25563877469669

    #Conversion ratios between latitude, longitude and pixels
    ralapi = abs(image1.size[0]/(lapuin-lapufi))
    ralopi = abs(image1.size[1]/(lopuin-lopufi))
          
    #Map colored according to the magnitudes of the events
    if mptype == 'magnitude':
    
        #Cycle that draws each event on the map
        for q in range(len(latitu)):
            
            #Check if the event happened on the map
            if abs(float(longit[q]))>abs(lopuin) or abs(float(longit[q]))<abs(lopufi) or abs(float(latitu[q]))>lapuin or abs(float(latitu[q]))<lapufi:
                dataap = []
                dataap.append('Fuera del mapa')
                inform = loc_sis(tuple((float(latitu[q]),float(longit[q]))))
                descri = 'A '+str(int(inform[1]))+'km de '+str(inform[0])+', '+str(inform[2])
                dataap.append(descri)
                region.append(dataap)
            else:
                inform = loc_sis(tuple((float(latitu[q]),float(longit[q]))))
                descri = 'A '+str(int(inform[1]))+'km de '+str(inform[0])+', '+str(inform[2])
                region.append(descri)
                x1 = int((float(longit[q])-lopuin)*ralopi)
                y1 = int(abs(float(latitu[q])-lapuin)*ralapi)
                r = 2.489035914*exp(0.3891820298*float(magnit[q]))
                #Draw and paint the events according to their magnitude
                if float(magnit[q])<4:
                    drawim.ellipse((x1-r,y1-r,x1+r,y1+r), fill='rgb(255,255,255)', outline='rgb(0,0,0)')
                elif float(magnit[q])>=4 and float(magnit[q])<5:
                    drawim.ellipse((x1-r,y1-r,x1+r,y1+r), fill='rgb(255,255,0)', outline='rgb(0,0,0)')
                elif float(magnit[q])>=5 and float(magnit[q])<6:
                    drawim.ellipse((x1-r,y1-r,x1+r,y1+r), fill='rgb(255,192,0)', outline='rgb(0,0,0)')
                elif float(magnit[q])>=6 and float(magnit[q])<7:
                    drawim.ellipse((x1-r,y1-r,x1+r,y1+r), fill='rgb(255,0,0)', outline='rgb(0,0,0)')
                else:
                    drawim.ellipse((x1-r,y1-r,x1+r,y1+r), fill='rgb(192,0,0)', outline='rgb(0,0,0)')
                    
        #Paste the appropiate legend
        x2 = 65
        y2 = 85
        image2 = Image.open(leyen1)
        image1.paste(image2,(x2,y2,x2+429,y2+364))
        
        #Map colored according to the depth of the events
    elif mptype == 'depth':

        #Cycle that draws each event on the map
        for q in range(len(latitu)):
            
        #Check if the event happened on the map
            if abs(float(longit[q]))>abs(lopuin) or abs(float(longit[q]))<abs(lopufi) or abs(float(latitu[q]))>lapuin or abs(float(latitu[q]))<lapufi:
                dataap = []
                dataap.append('Fuera del mapa')
                inform = loc_sis(tuple((float(latitu[q]),float(longit[q]))))
                descri = 'A '+str(int(inform[1]))+'km de '+str(inform[0])+', '+str(inform[2])
                dataap.append(descri)
                region.append(dataap)
            else:
                inform = loc_sis(tuple((float(latitu[q]),float(longit[q]))))
                descri = 'A '+str(int(inform[1]))+'km de '+str(inform[0])+', '+str(inform[2])
                region.append(descri)
                x1 = int((float(longit[q])-lopuin)*ralopi)
                y1 = int(abs(float(latitu[q])-lapuin)*ralapi)
                r = 2.489035914*exp(0.3891820298*float(magnit[q]))
                #Draw and paint the events according to their depth
                if float(edepth[q])<=10:
                    drawim.ellipse((x1-r,y1-r,x1+r,y1+r), fill='rgb(255,255,255)', outline='rgb(0,0,0)')
                elif float(edepth[q])>10 and float(edepth[q])<=30:
                    drawim.ellipse((x1-r,y1-r,x1+r,y1+r), fill='rgb(70,255,225)', outline='rgb(0,0,0)')
                elif float(edepth[q])>30 and float(edepth[q])<=70:
                    drawim.ellipse((x1-r,y1-r,x1+r,y1+r), fill='rgb(73,198,240)', outline='rgb(0,0,0)')
                elif float(edepth[q])>70 and float(edepth[q])<=150:
                    drawim.ellipse((x1-r,y1-r,x1+r,y1+r), fill='rgb(0,112,192)', outline='rgb(0,0,0)')
                else:
                    drawim.ellipse((x1-r,y1-r,x1+r,y1+r), fill='rgb(0,32,96)', outline='rgb(0,0,0)')
                
                #Paste the appropiate legend
                x2 = 65
                y2 = 85
                image2 = Image.open(leyen2)
                image1.paste(image2,(x2,y2,x2+427,y2+366))

    #Map with the events (one color)
    else:

        #Cycle that draws each event on the map
        for q in range(len(latitu)):

            #Check if the event happened on the map
            if abs(float(longit[q]))>abs(lopuin) or abs(float(longit[q]))<abs(lopufi) or abs(float(latitu[q]))>lapuin or abs(float(latitu[q]))<lapufi:
                dataap = []
                dataap.append('Fuera del mapa')
                inform = loc_sis(tuple((float(latitu[q]),float(longit[q]))))
                descri = 'A '+str(int(inform[1]))+'km de '+str(inform[0])+', '+str(inform[2])
                dataap.append(descri)
                region.append(dataap)
            else:
                #Draw the events
                inform = loc_sis(tuple((float(latitu[q]),float(longit[q]))))
                descri = 'A '+str(int(inform[1]))+'km de '+str(inform[0])+', '+str(inform[2])
                region.append(descri)
                x1 = int((float(longit[q])-lopuin)*ralopi)
                y1 = int(abs(float(latitu[q])-lapuin)*ralapi)
                r = 2.489035914*exp(0.3891820298*float(magnit[q]))
                drawim.ellipse((x1-r,y1-r,x1+r,y1+r), fill='rgb(70,140,240)', outline='rgb(0,0,0)')
    
    #Paste the world map
    x3 = 1650
    y3 = 85
    image2 = Image.open(mapmun)
    image1.paste(image2,(x3,y3, x3+468, y3+354))

    #Drawing coordinate system
    linlon = 15
    linwid = 4
    #Latitude
    corlat = []
    for a in range(min(int(lapuin), int(lapufi)), max(int(lapuin), int(lapufi))+1):
        corlat.append(a)
    
    for b in corlat:
        y = int(abs(float(b)-lapuin)*ralapi)
        drawim.line((0,y,linlon,y), fill='rgb(0,0,0)', width=linwid)
        drawim.line((image1.size[1]-linlon,y,image1.size[1],y), fill='rgb(0,0,0)', width=linwid)

    #Longitude
    corlon = []
    for a in range(min(int(lopuin), int(lopufi)), max(int(lopuin), int(lopufi))+1):
        corlon.append(a)
    
    for b in corlon:
        x = int(abs(float(b)-lopuin)*ralopi)
        drawim.line((x,0,x,linlon), fill='rgb(0,0,0)', width=5)
        drawim.line((x,image1.size[0],x,image1.size[0]-linlon), fill='rgb(0,0,0)', width=linwid)

    #Save the image of the map
    if mptype == "magnitude":    
        image1.save('Mapa de informe (magnitud) '+indate+' al '+fidate+'.png', 'PNG')
    elif mptype == "depth":
        image1.save('Mapa de informe (profundidad) '+indate+' al '+fidate+'.png', 'PNG')
    else:
        image1.save('Mapa de informe'+indate+' al '+fidate+'.png', 'PNG')

    #Cycle that creates the file with all the information extracted in txt
    fifile = open('Datos informe '+indate+' al '+fidate+'.txt', 'w')
    
    for p in range(len(utctim)):
        if type(region[p])==list:
            fifile.write('\n'+str(p+1).zfill(3)+','+utctim[p]+','+loctim[p]+','+latitu[p]+','+longit[p]+','+edepth[p]+','+residu[p]+','+usstat[p]+','+magnit[p]+','+imagni[p]+','+region[p][0])
        else:
            fifile.write('\n'+str(p+1).zfill(3)+','+utctim[p]+','+loctim[p]+','+latitu[p]+','+longit[p]+','+edepth[p]+','+residu[p]+','+usstat[p]+','+magnit[p]+','+imagni[p]+','+region[p])            

    #Cycle that creates the file with all the information extracted in JASON
    fifile = open('eventos.json', 'w')
    
    fifile.write('[')
    
    for p in range(len(utctim)):
        if p == (len(utctim)-1):
            if type(region[p])==list:
                fifile.write('{')
                fifile.write('"id": "'+evnumb[p]+'", "depth": "'+str(format(round(float(edepth[p]),3), '.3f'))+'", "longtime": "'+loctim[p]+'", "mag": "'+str(format(round(float(magnit[p]),3), '.2f'))+'", "lat": "'+str(format(round(float(latitu[p]),3), '.3f'))+'", "lon": "'+str(format(round(float(longit[p]),3), '.3f'))+'", "loc": "'+region[p][1]+'"')
                fifile.write('}')
            else:
                fifile.write('{')
                fifile.write('"id": "'+evnumb[p]+'", "depth": "'+str(format(round(float(edepth[p]),3), '.3f'))+'", "longtime": "'+loctim[p]+'", "mag": "'+str(format(round(float(magnit[p]),3), '.2f'))+'", "lat": "'+str(format(round(float(latitu[p]),3), '.3f'))+'", "lon": "'+str(format(round(float(longit[p]),3), '.3f'))+'", "loc": "'+region[p]+'"')
                fifile.write('}')
        else:
            if type(region[p])==list:
                fifile.write('{')
                fifile.write('"id": "'+evnumb[p]+'", "depth": "'+str(format(round(float(edepth[p]),3), '.3f'))+'", "longtime": "'+loctim[p]+'", "mag": "'+str(format(round(float(magnit[p]),3), '.2f'))+'", "lat": "'+str(format(round(float(latitu[p]),3), '.3f'))+'", "lon": "'+str(format(round(float(longit[p]),3), '.3f'))+'", "loc": "'+region[p][1]+'"')
                fifile.write('},') 
            else:
                fifile.write('{')
                fifile.write('"id": "'+evnumb[p]+'", "depth": "'+str(format(round(float(edepth[p]),3), '.3f'))+'", "longtime": "'+loctim[p]+'", "mag": "'+str(format(round(float(magnit[p]),3), '.2f'))+'", "lat": "'+str(format(round(float(latitu[p]),3), '.3f'))+'", "lon": "'+str(format(round(float(longit[p]),3), '.3f'))+'", "loc": "'+region[p]+'"')
                fifile.write('},')     

    fifile.write(']')
    fifile.close()


def event_extractor(event_code):
    #Date input
    evname = event_code
    
    #Directories of images
    mapmun = 'map_files/mapa_mundial.png'
    mapreg = 'map_files/mapa_regional.png'
    plabss = 'map_files/plantilla_BSS.png'
    
    #Variables used in the program
    evorid = []
    evnumb = []
    templi = []
    
    #Variables that store the information
    utctim = []
    loctim = []
    latitu = []
    longit = []
    edepth = []
    residu = []
    usstat = []
    magnit = []
    imagni = []
    region = []
    
    cumnth = int(evname[5:7])
    
    allday = []
    
    for i in listdir(evname[0:4]+'/'+str(cumnth).zfill(2)):
        allday.append(i)

    for j in allday:
        if j[8:11] == evname[8:11]:        
            direct = j
        
        else:
            pass

    #Cycle that enters the folder and analyzes all the files of the event it contains
    for k in listdir(evname[0:4]+'/'+str(cumnth).zfill(2)+'/'+direct):
        if k[9:15] == 'origin':
            evnumb = k[0:8]
        
            cufile = open(evname[0:4]+'/'+str(cumnth).zfill(2)+'/'+direct+'/'+k)

            #Cycle that runs through the file and extracts the origin time, latitude, longitude, depth and id of the event
            for l in cufile:
                if l[0] == '-':
                    pass
                else:
                    try:
                        utctim.index(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(l[31:47])+6*3600)))
                    except:                         
                        utctim.append(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(l[31:47])+6*3600)))
                        loctim.append(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(l[31:47]))))
                        latitu.append(l[2:9])
                        longit.append('-'+l[12:19])
                        edepth.append(l[21:29])
                                            
                        evorid.append(l[51:56])
    
        else:
            pass

    #Cycle that opens the origerr file and extracts the RMS of the solution for the event
    cufile = open(evname[0:4]+'/'+str(cumnth).zfill(2)+'/'+direct+'/'+evnumb+'.origerr')
            
    for m in cufile:
        if int(m[0:8]) == int(evorid[-1]):
            residu.append(m[172:178])
                
        else:
            pass
            
    #Cycle that opens the assoc file and extracts the amount of stations used to locate the event
    cufile = open(evname[0:4]+'/'+str(cumnth).zfill(2)+'/'+direct+'/'+evnumb+'.assoc')
            
    for n in cufile:
        try:
            templi.index(n[18:22])
                    
        except:
            if n[18:22] != '-   ' and n[12:17] == evorid[-1]:
                templi.append(n[18:22])
                        
            else:
                pass
            
    usstat.append(str(len(templi)))
    templi = []
            
    #Cycle that opens the netmag file and extracts the magnitude of the event and its uncertainty
    cufile = open(evname[0:4]+'/'+str(cumnth).zfill(2)+'/'+direct+'/'+evnumb+'.netmag')
            
    for o in cufile:
        if int(o[18:26]) == int(evorid[-1]):
            magnit.append(o[55:59])
            imagni.append(o[63:67])
                    
        else:
            pass

    #Cycle that creates the map with all the locations and magnitudes of the events extracted
            
    #Original map
    image1 = Image.open(mapreg)
    drawim = ImageDraw.Draw(image1)

    #Latitudes and longitudes of the initial and final points of the map
    lapuin = 18.8613689546248
    lopuin = -94.2427589202773

    lapufi = 12.18602717452006
    lopufi = -87.25563877469669

    #Conversion ratios between latitude, longitude and pixels
    ralapi = abs(image1.size[0]/(lapuin-lapufi))
    ralopi = abs(image1.size[1]/(lopuin-lopufi))

    #Cycle that draws each event on the map
    for q in range(len(latitu)):

        #Check if the event happened on the map
        if abs(float(longit[q]))>abs(lopuin) or abs(float(longit[q]))<abs(lopufi) or abs(float(latitu[q]))>lapuin or abs(float(latitu[q]))<lapufi:
            region.append('Fuera del mapa')
            pass
        else:
            #Draw the events
            region.append('-')
            x1 = int((float(longit[q])-lopuin)*ralopi)
            y1 = int(abs(float(latitu[q])-lapuin)*ralapi)
            r = 2.489035914*exp(0.3891820298*float(magnit[q]))
            drawim.ellipse((x1-r,y1-r,x1+r,y1+r), fill='rgb(70,140,240)', outline='rgb(0,0,0)')
    
    #Paste the world map
    x3 = 1650
    y3 = 85
    image2 = Image.open(mapmun)
    image1.paste(image2,(x3,y3, x3+468, y3+354))
    
    #Create document
    image3 = Image.open(plabss)
    
    #Fonts
    lfont1 = ImageFont.truetype('map_files/raleway/Raleway-Bold.ttf',100)
    lfont2 = ImageFont.truetype('map_files/raleway/Raleway-SemiBold.ttf',75)
    lfont3 = ImageFont.truetype('map_files/raleway/Raleway-Regular.ttf',60)
    lfont4 = ImageFont.truetype('map_files/raleway/Raleway-Regular.ttf',50)
    
    #Title
    drawim = ImageDraw.Draw(image3)
    drawim.text((860,400),'EVENTO SÍSMICO',(158,158,158),font=lfont1)
    
    #General data
    drawim.text((260,600),'Datos generales',(32,68,150),font=lfont2)
    
    drawim.text((260,700),'Fecha: '+loctim[0][0:10],(35,35,35),font=lfont3)
    
    drawim.text((260,775),'Tiempo de origen (local): '+loctim[0][11:19],(35,35,35),font=lfont3)
    
    drawim.text((260,850),'Magnitud: '+magnit[0]+' Ml',(35,35,35),font=lfont3)
    
    
    #Location
    drawim.text((1600,600),'Localización',(32,68,150),font=lfont2)
    
    drawim.text((1600,700),'Latitud: '+str(round(float(latitu[0]),3))+'°',(35,35,35),font=lfont3)
    
    drawim.text((1600,775),'Longitud: '+str(round(float(longit[0]),3))+'°',(35,35,35),font=lfont3)
    
    drawim.text((1600,850),'Profundidad: '+str(round(float(edepth[0]),3))+'km',(35,35,35),font=lfont3)
    
    #Note
    drawim.text((260,3050),'*Información preliminar',(35,35,35),font=lfont4)

    x4 = 275
    y4 = 1000
    
    #Gray square
    drawim.rectangle((x4-15,y4-15,x4+2015,y4+2015 ), fill=(128,128,128))
    
    #Map
    image1 = image1.resize((2000,2000))
    image3.paste(image1,(x4,y4,x4+2000,y4+2000))
    image3.save('Boletin evento '+evname+'.png', 'PNG')


def copia_dbevproc(event_code):
    '''
    Corrige la tabla y copia dbevproc al directorio
    '''
    
    #Get current directory
    cuyear = event_code[:4]
    cumnth = event_code[5:7]
    drctry = os.getcwd() + "/" + cuyear + '/' + cumnth + '/' + event_code

    #Copy dbevproc to the desired directory
    shutil.copy('dbevproc.pf',drctry)
    evdata = []
    
    #Cycles that read, edit and save the data from the site table
    archivos = os.listdir(drctry)

    for i in archivos:
        if i[9:] == '.site':
            with open(drctry + '/' + i, 'r') as site:
                for line in site:
                    if line[:4]=='XELA':
                        line = line[:48] + '2.4200 ' +line[55:]
                        x = i
                        evdata.append(line)
                        
                    else:
                        evdata.append(line)

    with open(drctry + '/' + x, 'w') as site:
        site.writelines(evdata)