

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

# Consistency check- Spelling mistake, different notation for same type examination and fixing it 
dups_df_CustomerDemographic = df_CustomerDemographic.pivot_table(index=['gender'], aggfunc='size')
# Mitigation
df_CustomerDemographic['gender'].replace(['F', 'Femal'], 'Female', inplace=True)
df_CustomerDemographic['gender'].replace(['M'], 'Male', inplace=True)
pd.unique(df_CustomerDemographic['gender'])

# missing data predection - DOB
df_CustomerDemographic.info()
real_dob = df_CustomerDemographic['DOB'].count()
missing_dob = len(df_CustomerDemographic['DOB']) - real_dob

#age calculation from DOB
now = pd.Timestamp('now')
df_CustomerDemographic['DOB'] = pd.to_datetime(df_CustomerDemographic['DOB'], format='%m%d%y') 
df_CustomerDemographic['DOB']  = df_CustomerDemographic['DOB'] .where(df_CustomerDemographic['DOB']  < now, df_3['DOB']  -  np.timedelta64(100, 'Y'))
df_CustomerDemographic['DOB']  = (now - df_CustomerDemographic['DOB'] ).astype('<m8[Y]') 

#Drop colum 'default' because the values dosent make sense
df_CustomerDemographic.drop(['default'], axis=1, inplace = True)


##Transanction dataset
df_Transactions.info()

#checking the prescence of the duplicate values 
df_Transactions.duplicated().sum()

#null value check
df_Transactions.isnull().sum()

#checking all orders are placed online
pd.Series(df_Transactions['online_order']).is_unique

#order status (apporved or cancelled)
df_Transactions.pivot_table(index=['order_status'], aggfunc='size')


#CustomerAddress dataset
df_CustomerAddress.info()
df_CustomerAddress.isnull().sum()
     
pd.Series(df_CustomerAddress['customer_id']).is_unique

df_CustomerAddress.pivot_table(index=['state'], aggfunc='size')

df_CustomerAddress['state'].replace(['New South Wales'], 'NSW', inplace=True)
df_CustomerAddress['state'].replace([ 'Victoria'], 'VIC', inplace=True)
