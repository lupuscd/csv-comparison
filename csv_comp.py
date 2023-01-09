import pandas as pd
import os

def csv_comp():
    # Read csv files from folder and combine the name and weight columns 
    # from each into a new csv file

    path = '/Users/invictus/Programing/Projects/csv comparison/new csv/'
    csv_path = '/Users/invictus/Programing/Projects/csv comparison/etf holdings/'
    filenames = [ f for f in os.listdir(csv_path) if f.endswith('.csv')]
    weight_list = ['Weight %', 'Weight (%)', 'Weight', '% of net assets', 'Weighting']
    name_list = ['Security', ' Security Description', 'Holding', 'Name', 'Security Name']

    dataframeslist = []

    for f in filenames:
        rpath = os.path.join(path, f)
        data = pd.read_csv(rpath,sep=';', on_bad_lines='skip', engine='python')
        existing_names = [clmn for clmn in name_list if clmn in data.columns]
        existing_weights = [wght for wght in weight_list if wght in data.columns]
        str_names = ''.join(existing_names)
        str_weights = ''.join(existing_weights)
        data = data.loc[:, [str_names, str_weights]]
        for index, row in data.iterrows():
            dataframeslist.append(list(row))    

    columns = ['Name', 'Weight (%)']
    fdata = pd.DataFrame(dataframeslist, columns=columns)
    fdata = fdata.dropna()
    fdata['Name'] = fdata['Name'].str.upper()
    fdata.to_csv('/Users/invictus/Programing/Projects/csv comparison/data/combined_data.csv',
    index = False)
