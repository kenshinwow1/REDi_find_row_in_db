import pandas as pd


df = pd.read_excel('/home/ualink/Desktop/xxx.xlsx')


value_in_E22 = df.at[21, 'E']

print("Value in the E22 cell:", value_in_E22)





