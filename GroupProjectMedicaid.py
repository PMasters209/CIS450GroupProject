# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 14:58:03 2020

@author: Paul Masterson
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

records = pd.read_csv('./State_Drug_Utilization_Data_2020.csv')
drugs = pd.read_csv('./product.csv')

##records = records.replace('UNKNOWN', value = np.nan)

realrec = records[records['Number of Prescriptions'].notna()]
realrec = realrec.replace('XX', value = np.nan)
realrec = realrec[realrec['State'].notna()]
realrec['Cost per Unit'] = realrec['Medicaid Amount Reimbursed'] / realrec['Units Reimbursed']
realrec.to_csv('CleanedRecords.csv', index = True, header = True)

#Which Drug is most prescribed?
grouped = realrec.groupby('Product Name').agg({'Units Reimbursed' : 'sum', 'Number of Prescriptions': 'sum' , 'Medicaid Amount Reimbursed' : 'mean', 'Non Medicaid Amount Reimbursed' : 'mean', 'Cost per Unit' : 'mean'})
sortbyDrug = grouped.sort_values(by=['Number of Prescriptions'], ascending = False)
sortbyDrug.to_csv('sortbyDrug.csv',index = True, header = True)

#Which drug is most expensive?
grouped = realrec.groupby('Product Name').agg({'Units Reimbursed' : 'sum', 'Number of Prescriptions': 'sum' , 'Medicaid Amount Reimbursed' : 'mean', 'Non Medicaid Amount Reimbursed' : 'mean', 'Cost per Unit' : 'mean'})
sortbyExpense = grouped.sort_values(by=['Cost per Unit'], ascending = False)

#States
grouped = realrec.groupby('State').agg({'Units Reimbursed' : 'sum', 'Number of Prescriptions': 'sum' , 'Medicaid Amount Reimbursed' : 'sum', 'Non Medicaid Amount Reimbursed' : 'sum',  'Cost per Unit' : 'sum'})
sortbyState = grouped.sort_values(by=['Medicaid Amount Reimbursed'], ascending = False)