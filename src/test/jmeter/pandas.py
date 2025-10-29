import pandas as pd
# from pandas import df
#  df = pd.read_csv('results/petclinic-test-results.jtl')
df = pd.read_csv('../../../results/petclinic-test-results.jtl')
print(df.describe())
