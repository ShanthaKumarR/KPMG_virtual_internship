

import pandas as pd 
import seaborn as sns
import numpy as np

#Load the data as pandas dataframe 

sheets = pd.read_excel('KPMG_VI_New_raw_data_update_final.xlsx', engine='openpyxl',
                       sheet_name = ['Transactions', 'NewCustomerList', 'CustomerDemographic', 'CustomerAddress'])
                       
 
df_Transactions = sheets['Transactions']
df_NewCustomerList = sheets['NewCustomerList']
df_CustomerDemographic = sheets['CustomerDemographic']
df_CustomerAddress = sheets['CustomerAddress']

#drop the coloumns which has only zeros 

df_Transactions.columns
df_NewCustomerList.columns
df_CustomerDemographic.columns
df_CustomerAddress.columns

# df_CustomerDemographic - Missing data visualization using see born

sns.heatmap(df_3.isnull(), yticklabels = False, cbar = False, cmap = 'viridis')

#Spelling mistake, different notation for same type examination and fixing it 

dups_df_CustomerDemographic = df_CustomerDemographic.pivot_table(index=['gender'], aggfunc='size')
df_CustomerDemographic['gender'].replace(['F', 'Femal'], 'Female', inplace=True)
df_CustomerDemographic['gender'].replace(['M'], 'Male', inplace=True)
pd.unique(df_CustomerDemographic['gender'])

# missing data predection - DOB
df_CustomerDemographic.info()
real_dob = df_CustomerDemographic['DOB'].count()
missing_dob = len(df_CustomerDemographic['DOB']) - real_dob

#Drop colum 'default' because the values dosent make sense
df_CustomerDemographic.drop(['default'], axis=1, inplace = True)
