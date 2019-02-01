import pandas as pd

#Use Python's Pandas library to read the excel file. Then skip the first 5 rows because that includes metadata that
#we do not want, also skip the last 7 lines as those only include metadata as well
divorceRate = pd.read_excel('state_divorce_rates_dirty.xlsx',
                            skiprows=5,
                            skipfooter=7,
                            na_values='---',
                            index_col=0)

#Pivote divorce rate and years so that they now represent their own column
divorceRate = divorceRate.stack()

#Change the name of the last column so that it reads Divorce rates and does not confuse the user
divorceRate.name = 'Divorce Rates'

#This line drops all the na values on the table of data
divorceRate.dropna(how='all', inplace=True)

#our column headers will now read: "State" & "Year"
divorceRate.index.names = ['State', 'Year']

#Write the transformed data to a new excel sheet to make sure the data was inputted properly
divorceRate.to_excel(excel_writer='state_divorce_rate_clean.xls',
                     sheet_name='Divorce Rates',
                     na_rep='null')


