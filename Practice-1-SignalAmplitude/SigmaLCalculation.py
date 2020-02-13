# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 22:13:00 2020

@author: Valeriia Shurupina
"""
import pandas as pd
import os


###### Functions

# Create a subdir for output plots
# check if subdirectory exists
def createSubdir(workspace, subdirList):
    for subdir in subdirList:
        if not os.path.isdir(workspace + '//' + subdir):
            os.mkdir(os.path.join(workspace, subdir))

# To open Workbook
def inputData(data_input):
    data = pd.read_excel(data_input, sheet_name=0, header=0)
    return data

# Create a new column for σl and calculate SigmaL
def calcSigmaL(data):
    # Copy dataframe for further modifications
    selected = data.loc[:]

    # Create a new column for σl
    selected["SigmaLSum"] = "0.0"

    # Look for SigmaLSum
    for val in selected:
        selected['SigmaLSum'] = (selected['C']) ** 2 + (selected['S']) ** 2

    # Sum SigmaLSums based on l and find square root, write into a new column
    selected['SigmaL'] = selected.groupby(['l'])['SigmaLSum'].transform(sum)

    # Find square root
    selected['SigmaL'] = selected['SigmaL'] ** 0.5
    return selected

# Initialization of dictionary with unique l values, Converting into list of tuples,
# From list of tuples to pandas DataFrame for export
def convToDataFrame(selected):
    # Initialization of dictionary with unique l values
    uniqueValuesDict = dict(zip(selected['l'], selected['SigmaL']))

    # Converting into list of tuples
    uniqueValuesList = [(k, v) for k, v in uniqueValuesDict.items()]

    # From list of tuples to pandas DataFrame for export
    sigmaL = pd.DataFrame(uniqueValuesList, columns=['l', 'SigmaL'])
    return sigmaL

# Write SigmaL into excel
def writeToExcel(sigmaL, data_output_name):
    data_output = sigmaL.to_excel(data_output_name)

# =======================================================

# Input nad Output files location
# Give the location of the file
workspace = 'C:/Users/Valeriia/YandexDisk/Studying/GitHub/SignalAmplitude'
subdirList = ['Plots', 'OutputTables', 'Input']
data_input = ("Input/GOCO03s_Spectral_Calculation.xlsx")
data_output_name = workspace + "/OutputTables/" + "SigmaLOutput.xlsx"

# Create a subdir for output plots
# check if subdirectory exists
createSubdir(workspace, subdirList)

# To open Workbook
data = inputData(data_input)

# Create a new column for σl and calculate SigmaL
selected = calcSigmaL(data)

# Initialization of dictionary with unique l values, Converting into list of tuples,
# From list of tuples to pandas DataFrame for export
sigmaL = convToDataFrame(selected)

# Write SigmaL into excel
writeToExcel(sigmaL, data_output_name)