import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def openExcel(fileName):
	return pd.read_excel(fileName)

def lookForColms(data, columsName):
	return pd.DataFrame(data, columns = columsName)

def scatterData(xValues, yValues, labelName = "", marker = "*"):
	plt.scatter(xValues, yValues, label = labelName, marker = marker)

def plotData(xValues, yValues, labelName = "", marker = "*"):
	pass

def showPlot():
	plt.show()


if __name__ == "__main__":
	data = openExcel("C:\\Users\\Mateusz\\Desktop\\simpleData\\data1.xlsx")
	dataFrame = lookForColms(data, ["Nr", "Value", "Serial Nr."])

	scatterData(dataFrame["Value"], dataFrame["Value"])

	showPlot()