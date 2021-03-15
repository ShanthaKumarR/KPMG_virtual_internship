import pandas as pd 
import seaborn as sns
import numpy as np

#Read the dataset
sheets = pd.read_excel('KPMG_VI_New_raw_data_update_final.xlsx', engine='openpyxl',
                       sheet_name = ['Transactions', 'NewCustomerList', 'CustomerDemographic', 'CustomerAddress'])

df_Transactions = sheets['Transactions']
df_NewCustomerList = sheets['NewCustomerList']
df_CustomerDemographic = sheets['CustomerDemographic']
df_CustomerAddress = sheets['CustomerAddress']

#Remove the columns with null values 
df_Transactions = df_Transactions.dropna(axis = 'columns', how = 'all')
df_NewCustomerList = df_NewCustomerList.dropna(axis = 'columns', how = 'all')
df_CustomerDemographic = df_CustomerDemographic.dropna(axis = 'columns', how = 'all')
df_CustomerAddress = df_CustomerAddress.dropna(axis = 'columns', how = 'all')

#Remove columns with unnamed attributes
df_NewCustomerList.columns
cols = ['Unnamed: 16','Unnamed: 17','Unnamed: 18','Unnamed: 19','Unnamed: 20']
df_NewCustomerList.drop(cols, axis=1, inplace = True)
print(df_NewCustomerList.columns)

#age calculation from DOB
now = pd.Timestamp('now')
df_CustomerDemographic['DOB'] = pd.to_datetime(df_CustomerDemographic['DOB'], format='%m%d%y') 
df_CustomerDemographic['DOB']  = df_CustomerDemographic['DOB'] .where(df_CustomerDemographic['DOB']  < now, df_CustomerDemographic['DOB']  -  np.timedelta64(100, 'Y'))
df_CustomerDemographic['DOB']  = (now - df_CustomerDemographic['DOB'] ).astype('<m8[Y]')
#print(df_CustomerDemographic.DOB)

#Drop colum 'default' because the values dosent make sense
df_CustomerDemographic.drop(['default'], axis=1, inplace = True)