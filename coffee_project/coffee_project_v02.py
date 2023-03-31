# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 16:42:21 2023

@author: sophi
"""

# 2023-03-25

# Classification of coffee spectra
# The file "FTIR_Spectra_instant_coffee.csv" contains a collection of 56 mid 
# infrared diffuse reflectance (MIR-DRIFT) spectra of lyophilized coffee 
# produced from two species: arabica (29 samples, '1') and canephora var. 
# robusta (27 samples, '2').


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create DataFrame

df = pd.read_csv("C:\\Users\\sophi\\Documents\\GitHub\\Spectroscopy\\coffee_project\\data\\FTIR_Spectra_instant_coffee_mod.csv")
print(df.head())

plt.plot(df['sample'][1:], df['1'][1:])
plt.show()