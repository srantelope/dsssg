#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 19:16:08 2019

@author: rt
"""

import os
import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf
college_path = os.path.join('a.csv')
college = pd.read_csv(college_path)
college.head()
#sns.pairplot(college, hue = 'mag')
#sns.distplot(df['mpg'], bins=20, rug=True, kde=True)