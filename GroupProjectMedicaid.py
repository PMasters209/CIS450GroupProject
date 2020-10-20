# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 14:58:03 2020

@author: Paul Masterson
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

records = pd.read_csv('./State_Drug_Utilization_Data_2020.csv')

##records = records.replace('UNKNOWN', value = np.nan)
realrec = records[records['Number of Prescriptions'].notna()]
#realrec = realrec[realrec['Product Name'].notna()]


grouped = realrec.groupby('Product Name').agg({'Units Reimbursed' : 'sum', 'Number of Prescriptions': 'sum' , 'Medicaid Amount Reimbursed' : 'sum', 'Non Medicaid Amount Reimbursed' : 'sum'})
sortHigh = grouped.sort_values(by=['Number of Prescriptions'], ascending = False)
sortHigh.to_csv('./exported.csv',index = True, header = True)