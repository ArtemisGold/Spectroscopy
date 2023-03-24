# 2023-03-24

# Classification of coffee spectra
# The file "FTIR_Spectra_instant_coffee.csv" contains a collection of 56 mid 
# infrared diffuse reflectance (MIR-DRIFT) spectra of lyophilized coffee 
# produced from two species: arabica (29 samples) and canephora var. 
# robusta (27 samples).

import numpy as np
import pandas as pd
#pd.options.display.max_columns = 8
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\sophi\\Documents\\GitHub\\Spectroscopy\\coffee_project\\data\\FTIR_Spectra_instant_coffee.csv")
df = df.transpose()
print(df.head(10))
print(df.describe())    