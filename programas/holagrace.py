#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 10:19:33 2019

@author: rt
"""

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

m = folium.Map(
    location=[14.4837, -90.6165],
    zoom_start=12.49,
    tiles='Stamen Terrain'
)
 
tooltip = 'Estaciones'
 

folium.RegularPolygonMarker([14.656791, -90.513590],radius=6,popup='CIRS', tooltip= 'CIRS', fill_color= "red",).add_to(m)
folium.RegularPolygonMarker([14.583379, -90.563163],radius=6,popup='CMONM', tooltip= 'CMONM', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.612077, -90.531148],radius=6,popup='CINGE', tooltip='CINGE', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.603462, -90.556828],radius=6,popup='CSTER', tooltip= 'CSTER', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.601179, -90.507591],radius=6,popup='CASUN', tooltip= 'CASUN', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.625451, -90.535709],radius=6,popup='KINAL', tooltip='KINAL', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.645901, -90.482818],radius=6,popup='INMAC', tooltip='INMAC', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.645764, -90.506287],radius=6,popup='ITC', tooltip='ITC', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.621175, -90.506287],radius=6,popup='EBENE', tooltip='EBENE', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.571435, -90.488360],radius=6,popup='JUAMA', tooltip='JUAMA', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.580317, -90.493987],radius=6,popup='EXCEL', tooltip='EXCEL', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.565562, -90.481552],radius=6,popup='CCONS', tooltip='CCONS', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.643623, -90.512750],radius=6,popup='IPRES', tooltip='IPRES', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.585361, -90.519335],radius=6,popup='TADEO', tooltip='TADEO', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.592330, -90.549728],radius=6,popup='CBIBL', tooltip='CBIBL', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.621267, -90.485237],radius=6,popup='CAUST', tooltip='CAUST', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.607997, -90.605162],radius=6,popup='LSECB', tooltip='LSECB', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.621250, -90.526782],radius=6,popup='SETEC', tooltip='SETEC', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.611841, -90.522356],radius=6,popup='ICREY', tooltip='ICREY', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.599252, -90.595946],radius=6,popup='ACRIS', tooltip='ACRIS', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.610883, -90.516014],radius=6,popup='SEUNI', tooltip='SEUNI', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.603847, -90.512817],radius=6,popup='ASEGG', tooltip='ASEGG', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.631369, -90.538801],radius=6,popup='AMGGT', tooltip='AMGGT', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.624119, -90.520709],radius=6,popup='CDBOS', tooltip='CDBOS', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.584082, -90.487881],radius=6,popup='RGIL', tooltip='RGIL', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.620449, -90.529321],radius=6,popup='JUNKA', tooltip='JUNKA', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.646869, -90.505732],radius=6,popup='CERRITO', tooltip= 'CERRITO', fill_color= "yellow",).add_to(m)
folium.RegularPolygonMarker([14.633094, -90.493736],radius=6,popup='ASUNCION', tooltip='ASUNCION', fill_color= "yellow").add_to(m)
folium.RegularPolygonMarker([14.479382, -90.485771],radius=6,popup='CBVH', tooltip='CBVH', fill_color= "yellow").add_to(m)
folium.RegularPolygonMarker([14.655844, -90.482753],radius=6,popup='ATLANTIDA', tooltip='ATLANTIDA', fill_color= "yellow").add_to(m)
folium.RegularPolygonMarker([14.646623, -90.582078],radius=6,popup='EMILIANI', tooltip='EMILIANI', fill_color= "yellow").add_to(m)
folium.RegularPolygonMarker([14.635141, -90.58817],radius=6,popup='BAYER', tooltip='BAYER', fill_color= "yellow").add_to(m)
folium.RegularPolygonMarker([14.633549, -90.576045],radius=6,popup='MERCK', tooltip='MERCK', fill_color= "yellow").add_to(m)
folium.RegularPolygonMarker([14.657463, -90.557504],radius=6,popup='NARANJO', tooltip='NARANJO', fill_color= "yellow").add_to(m)
folium.RegularPolygonMarker([14.616708, -90.633316],radius=6,popup='ALUX', tooltip= 'ALUX',fill_color= "yellow").add_to(m)
folium.RegularPolygonMarker([14.551155, -90.523189],radius=6,popup='BOCA', tooltip='BOCA', fill_color= "yellow").add_to(m)
folium.RegularPolygonMarker([14.521536, -90.564489],radius=6,popup='FRUTAL', tooltip='FRUTAL', fill_color= "yellow").add_to(m)
folium.RegularPolygonMarker([14.5569, -90.550946],radius=6,popup='TIPIC', tooltip='TIPIC', fill_color= "yellow").add_to(m)
folium.RegularPolygonMarker([14.560225, -90.544975],radius=6,popup='COLGATE', tooltip='COLGATE', fill_color= "yellow").add_to(m)
folium.RegularPolygonMarker([14.657466, -90.577429],radius=6,popup='PARROQUIA', tooltip='PARROQUIA', fill_color= "yellow").add_to(m)
folium.RegularPolygonMarker([14.60143, -90.517853],radius=6,popup='UNIONCH', tooltip='UNIONCH', fill_color= "yellow").add_to(m)
folium.RegularPolygonMarker([14.664995, -90.494472],radius=6,popup='CMPROG', tooltip='CMPROG', fill_color= "yellow").add_to(m)
folium.RegularPolygonMarker([14.638611, -90.516765],radius=6,popup='ALEMAN', tooltip='ALEMAN', fill_color= "yellow").add_to(m)
folium.RegularPolygonMarker([14.60143, -90.517853],radius=6,popup='PARROQUIAZ6', tooltip='PARROQUIAZ6', fill_color= "yellow").add_to(m)
folium.RegularPolygonMarker([14.958048, -91.80232],radius=6,popup='SMARC', tooltip= 'SMARC', fill_color= "red",).add_to(m)
folium.RegularPolygonMarker([15.316158, -91.485137],radius=6,popup='HUEH', tooltip= 'HUEH', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.504133, -90.613072],radius=6,popup='VILL', tooltip='VILL', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.861836, -91.549114],radius=6,popup='XELA', tooltip= 'XELA', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.283200, -89.897520],radius=6,popup='JUTI', tooltip= 'JUTI', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.557461, -90.729739],radius=6,popup='ANTIG', tooltip='ANTIG', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.544712, -90.445655],radius=6,popup='SJPIN', tooltip='SJPIN', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([15.471589, -90.376722],radius=6,popup='COBAN', tooltip='COBAN', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.294576, -91.913988],radius=6,popup='CHAMP', tooltip='CHAMP', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([15.721002, -88.597682],radius=6,popup='IZABA', tooltip='IZABA', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([15.100999, -90.317875],radius=6,popup='SALAM', tooltip='SALAM', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.855878, -90.068851],radius=6,popup='GUAST', tooltip='GUAST', fill_color= "yellow").add_to(m)
folium.RegularPolygonMarker([15.53228, -89.328446],radius=6,popup='ELEST', tooltip= 'ELEST', fill_color= "yellow",).add_to(m)
folium.RegularPolygonMarker([14.798673, -89.546461],radius=6,popup='CHIQUI', tooltip= 'CHIQUI', fill_color= "yellow").add_to(m)
folium.RegularPolygonMarker([14.273674, -90.776012],radius=6,popup='ESQUI', tooltip='ESQUI', fill_color= "yellow").add_to(m)
folium.RegularPolygonMarker([15.030043, -91.14416],radius=6,popup='QUICH', tooltip= 'QUICH', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.536051, -91.682776],radius=6,popup='RETAL', tooltip='RETAL', fill_color= "yellow").add_to(m)
folium.RegularPolygonMarker([14.635612, -89.990183],radius=6,popup='JALA', tooltip='JALA', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.085721, -90.378871],radius=6,popup='STARS', tooltip='STARS', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([14.699306, -91.864172],radius=6,popup='COATE', tooltip='COATE', fill_color= "yellow").add_to(m)
folium.RegularPolygonMarker([14.534745, -91.510632],radius=6,popup='MAZA', tooltip='MAZA', fill_color= "yellow").add_to(m)
folium.RegularPolygonMarker([14.77184, -91.183786],radius=6,popup='SOLO', tooltip='SOLO', fill_color= "yellow").add_to(m)
folium.RegularPolygonMarker([14.530458, -92.221666],radius=6,popup='OCOS', tooltip='OCOS', fill_color= "yellow").add_to(m)
folium.RegularPolygonMarker([13.915157, -90.888111],radius=6,popup='CHULA', tooltip='CHULA', fill_color= "red").add_to(m)
folium.RegularPolygonMarker([13.750794, -90.119605],radius=6,popup='FARO', tooltip='FARO', fill_color= "yellow").add_to(m)
folium.RegularPolygonMarker([15.988342, -90.782019],radius=6,popup='IXCAN', tooltip='IXCAN', fill_color= "yellow").add_to(m)
folium.RegularPolygonMarker([14.628875, -89.443552],radius=6,popup='QUETZ', tooltip='QUETZ', fill_color= "yellow").add_to(m)
folium.RegularPolygonMarker([13.890154, -90.481798],radius=6,popup='MONTE', tooltip='MONTE', fill_color= "yellow").add_to(m)
folium.RegularPolygonMarker([14.971879, -89.540751],radius=6,popup='ZACA', tooltip='ZACA', fill_color= "red").add_to(m)

dibujar_lineas_guia(m)
m.save("Estaciones.html")
