import plotly.express as px
import csv
import numpy as np

def getdatasource(datapath):
    Coffee=[]
    sleep=[]
    with open (datapath) as csvfile:
        cvsreader=csv.DictReader(csvfile)
        for row in cvsreader:
            Coffee.append(float(row['Coffee in ml']))
            sleep.append(float(row['sleep in hours']))
    return {'x':Coffee,'y':sleep}

def findcorealation(datasource):
    corelation=np.corrcoef(datasource['x'],datasource['y'])
    print('corelation between cups of coffee and hours of sleep is --> ',corelation[0,1])

def setup():
    datapath='cups of coffee vs hours of sleep.csv'
    datasource=getdatasource(datapath)
    findcorealation(datasource)

setup()