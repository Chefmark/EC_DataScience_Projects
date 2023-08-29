import pandas as pd
urls = [
    'https://raw.githubusercontent.com/evahegnar/SSBI/main/Assignment/Transactions/Bulgaria.csv', 
    'https://raw.githubusercontent.com/evahegnar/SSBI/main/Assignment/Transactions/Canada.csv',
    'https://raw.githubusercontent.com/evahegnar/SSBI/main/Assignment/Transactions/China.csv',
    'https://raw.githubusercontent.com/evahegnar/SSBI/main/Assignment/Transactions/Ecuador.csv',
    'https://raw.githubusercontent.com/evahegnar/SSBI/main/Assignment/Transactions/Egypt.csv',
    'https://raw.githubusercontent.com/evahegnar/SSBI/main/Assignment/Transactions/France.csv',
    'https://raw.githubusercontent.com/evahegnar/SSBI/main/Assignment/Transactions/Georgia.csv',
    'https://raw.githubusercontent.com/evahegnar/SSBI/main/Assignment/Transactions/Germany.csv',
    'https://raw.githubusercontent.com/evahegnar/SSBI/main/Assignment/Transactions/Iceland.csv',
    'https://raw.githubusercontent.com/evahegnar/SSBI/main/Assignment/Transactions/Japan.csv',
    'https://raw.githubusercontent.com/evahegnar/SSBI/main/Assignment/Transactions/Sweden.csv',
    'https://raw.githubusercontent.com/evahegnar/SSBI/main/Assignment/Transactions/Vietnam.csv',
    'https://raw.githubusercontent.com/evahegnar/SSBI/main/Assignment/Transactions/Zimbabwe.csv',
        ]

df_list = []

for url in urls:
    df = pd.read_csv(url, index_col = None, header=None)
    df_list.append(df)

df_master = pd.concat(df_list, sort = False)
df_master = df_master.drop_duplicates().reset_index(drop=True)
print(df_master)