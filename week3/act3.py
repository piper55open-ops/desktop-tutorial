import pandas as pd
class compute:
    def __init__(self):
        self.df = pd.read_csv('wdbc.csv', header=None)
        self.df.to_parquet('wddvc.parquet')
        self.parquet_file = 'wddvc.parquet'

    def jisuan(self):
        df_parquet = pd.read_parquet(self.parquet_file)
        print("There are", len(df_parquet.columns) - 2, "columns. Which column (1-30) do you want to get data from?")
        a = int(input())
        print("Maximum value:", df_parquet[a + 1].max())
        print("Minimum value:", df_parquet[a + 1].min())
        print("Mean value:", df_parquet[a + 1].mean())
        print("Absolute values:")
        print(df_parquet[a+1].abs())


a=compute()
a.jisuan()
