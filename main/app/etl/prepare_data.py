from pandas import read_csv

dataPath = 'app/data/Google.csv'

df = read_csv(dataPath)
df['Date'] = df['Date'].astype('datetime64')

col = "Date Open High Low Close Volume Ex_Dividend Split_Ratio Adj_Open Adj_High Adj_Low Adj_Close Adj_Volume"
df.columns = col.split(" ")

