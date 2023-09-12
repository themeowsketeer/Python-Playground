# import requests

import pandas as pd

import numpy as np

## URL to main server of IMF

# url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/'

# # Key dataset to scarp
# key = 'CompactData/IFS/M.GB.PMP_IX'

# data = requests.get(f'{url}{key}').json()['CompactData']['DataSet']['Series']

# baseYear = data['@BASE_YEAR']

# # Create data mainframe from the observation

# dataList = [[obs.get('@TIME_PERIOD'),
#              obs.get('@OBS_VALUE')] 
#              for obs in data['Obs']]

dataList = pd.read_csv('Gross_domestic_product_constant.csv')

dataFrame = pd.DataFrame(dataList)

# dataFrame = pd.DataFrame(dataList, columns=['Date', 'Value'])

# dataFrame = dataFrame.set_index(pd.to_datetime(dataFrame['Date']))['Value'].astype(float)

# # Detect any NULL value in the dataset and replace with 0
# dataFrame[pd.isna(dataFrame)] = 0

# csvSave = open('sample.csv','w')

# dataFrame.to_csv('sample.csv', header = True)

# Drop any columns with all value being NaN
dataFrame = dataFrame.dropna(axis=1, how='all')

print(dataFrame)