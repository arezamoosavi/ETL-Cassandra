from pandas import read_csv

dataPath = 'app/data/Google.csv'

df = read_csv(dataPath)
df['Date'] = df['Date'].astype('datetime64')

col = "date open high low close volume ex_dividend split_ratio adj_open adj_high adj_low adj_close adj_volume"
df.columns = col.split(" ")

