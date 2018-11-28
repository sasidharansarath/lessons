# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 12:15:45 2018

@author: Sarath Sasidharan
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

survey = pd.read_excel(r"C:\Users\Sarath Sasidharan\Desktop\Stefanie_Data\BBD Survey Data_Clean.xlsx")

corr_ = survey.corr()

corr_.to_excel(r"C:\Users\Sarath Sasidharan\Desktop\Stefanie_Data\Correlation.xlsx")
