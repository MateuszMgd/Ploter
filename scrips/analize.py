import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def openExcel(fileName):
	return pd.read_excel(fileName)

def lookForColms(data, columsName):
	return pd.DataFrame(data, columns = columsName)

def scatterData(xValues, yValues, labelName = "Yes", marker = "*"):
	plt.scatter(xValues, yValues, label = labelName, marker = marker)

def showPlot():
	plt.show()