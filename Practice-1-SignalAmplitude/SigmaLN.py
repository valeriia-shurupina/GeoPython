# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:09:33 2020

@author: Valeriia Shurupina
"""
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

# Earth Radius, m
R = 6378136.3

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
    # Copy dataframe for further modifications
    selected = data.iloc[:, 1:3]
    return selected

# Create a new column for σl(N) and calculate σl(N) = SigmaLN
def calcSigmaLN(selected):
    # Create a new column for σl(N)
    selected["SigmaLN"] = "0.0"
    # Look for σl(N) = SigmaLN
    for val in selected:
        selected['SigmaLN'] = (selected['SigmaL']) * R
    return selected

# Write SigmaLN into excel
def writeToExcel(selected_calculated, data_output_name):
    data_output = selected_calculated.to_excel(data_output_name)

# Plot SigmaL
def plotSigmaL(selected):
    SigmaLNPlot = selected.loc[:, 'SigmaLN']

    # Finding data bounds
    length = len(SigmaLNPlot) - 1
    min_SigmaLNPlot = min(SigmaLNPlot)
    max_SigmaLNPlot = max(SigmaLNPlot)
    max_SigmaLNPlot = max_SigmaLNPlot - R + 20

    # Creating subplot and defining its size (inches)
    fig, axe = plt.subplots(figsize=(7, 5), constrained_layout=True);

    # log scale
    plt.plot(length, max_SigmaLNPlot)
    plt.yscale('log')

    # Set figure title
    fig.suptitle('Signal amplitude per degree of GOCO03s', fontweight='bold',
                 fontfamily='Verdana')

    # Axis labels
    axe.set_xlabel('Spherical harmonic degree', style='italic')  # l
    axe.set_ylabel('Geoid height, m', style='italic')  # σl(N)

    # Set plot line width
    line_width = 1.5

    # Don't allow the axis to be on top of your data
    axe.set_axisbelow(True)

    # Customize the major grid
    axe.grid(which='major', linestyle='-', linewidth='0.5', color='black')
    # Customize the minor grid
    axe.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

    # Turn on the minor TICKS, which are required for the minor GRID
    axe.minorticks_on()

    # Plot data
    plot = SigmaLNPlot.plot(ax=axe, c='orange', lw=line_width,
                     ylim=[min_SigmaLNPlot + 0.001, max_SigmaLNPlot],
                     xlim=[min_SigmaLNPlot, length],
                     grid=True)

    return plot

# =======================================================

# Input nad Output files location
# Give the location of the file
workspace = 'C:/Users/Valeriia/YandexDisk/Studying/GitHub/SignalAmplitude'
subdirList = ['Plots', 'OutputTables', 'Input']
data_input = workspace + "/OutputTables/" + "SigmaLOutput.xlsx"
data_output_name = workspace + "/OutputTables/" + "SigmaLNOutput.xlsx"
plot_png_output = workspace + "/Plots/" + "SignalAmplitudesPerDegree.png"
plot_pdf_output = workspace + "/Plots/" + "SignalAmplitudesPerDegree.pdf"

# Create folders for Outputs
createSubdir(workspace, subdirList)

# To open Workbook and copy dataframe for further modifications
selected = inputData(data_input)

# Create a new column for σl(N) and calculate σl(N) = SigmaLN
selected_calculated = calcSigmaLN(selected)

# Write SigmaLN into excel
writeToExcel(selected_calculated, data_output_name)

# Plot SigmaL
plot = plotSigmaL(selected)

# Export plot as PNG
plot.get_figure().savefig(plot_png_output)

# Export plot as PDF
plot.get_figure().savefig(plot_pdf_output)