import plotly.express as px
import csv
import numpy as np

def getdatasource(datapath):
    MarksInPercentage=[]
    DaysPresent=[]
    with open (datapath) as csvfile:
        cvsreader=csv.DictReader(csvfile)
        for row in cvsreader:
            MarksInPercentage.append(float(row['Marks In Percentage']))
            DaysPresent.append(float(row['Days Present']))
    return {'x':MarksInPercentage,'y':DaysPresent}

def findcorealation(datasource):
    corelation=np.corrcoef(datasource['x'],datasource['y'])
    print('corelation between student marks and days persent is --> ',corelation[0,1])

def setup():
    datapath='Student Marks vs Days Present.csv'
    datasource=getdatasource(datapath)
    findcorealation(datasource)

setup()