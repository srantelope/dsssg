#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 17:51:42 2020

@author: rt
"""
import numpy as np
import os
import geophysics
from geophysics import estacion, distancia2

fac02 = [('ACRIS', 5.23487983),('CAUST', 4.5061185), ('CDBOS',1.99498195), ('CSTER', 3.2735276), ('EXCEL', 3.83000264),('ITC', 1.54168501), ('JUAMA',3.74953781), ('LSECB', 6.60771195), ('RGIL', 1.99568624), ('SEUNI',2.8355489), ('SJPIN',4.43542565), ('VILL', 7.09736773)] 

lat = []
lon = []


for i in fac02:
    est = estacion(i[0])
    lat.append(est.latitud)
    lon.append(est.longitud)