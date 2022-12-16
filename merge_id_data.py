import pandas as pd

# Group and merge identical items in the combined_data csv file

data = pd.read_csv('/Users/invictus/Programing/Projects/csv comparison/data/combined_data.csv')

gdata = data.groupby(['Name'], as_index=False, sort=False).agg({'Weight (%)':'sum'})
#.sort_values(by='Weight (%)')
gdata.to_csv('/Users/invictus/Programing/Projects/csv comparison/data/grouped_data.csv',
 index = False)
