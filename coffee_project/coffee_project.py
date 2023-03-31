# 2023-03-24

# Classification of coffee spectra
# The file "FTIR_Spectra_instant_coffee.csv" contains a collection of 56 mid 
# infrared diffuse reflectance (MIR-DRIFT) spectra of lyophilized coffee 
# produced from two species: arabica (29 samples, '1') and canephora var. 
# robusta (27 samples, '2').


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create DataFrame

df = pd.read_csv("C:\\Users\\sophi\\Documents\\GitHub\\Spectroscopy\\coffee_project\\data\\FTIR_Spectra_instant_coffee.csv")

df.rename(columns = {'Sample Number:':'sample'}, inplace=True)
df.set_index('sample', inplace=True)
df_t = df.transpose()
df_t.drop(df_t.columns[[1]], axis=1, inplace=True)
df_t.rename(columns = {'Group Code:':'target'}, inplace=True)

print(df_t.head(10)) 

# Define X and y

X_data = pd.DataFrame(df_t.drop(['target'], axis=1))
y_data = df_t['target'] # Alternative to pd series: .value returns ndarray

print(X_data.head())
print(y_data)



