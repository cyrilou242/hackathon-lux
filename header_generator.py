"""LUX AI
Timo Johann, Cyril de Catheu
05/18/2018
Purpose of the file : Script to generate attributes on processed binarized data.
"""

import pandas as pd
import csv

def genarate_headers(filename):
    df = pd.read_csv(filename)
    s=""


    for i in range(len(df.columns)):
        s += "attr" + str(i) + ','
        print(i)

    s = s[:-1]

    return s
