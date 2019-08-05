import csv
import json
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

##function to convery csv file to json file
def csv_to_json(csvf,jsonf):
        rows = []
        with open(file) as csvfile:
                reader = csv.DictReader(csvfile)
                field = reader.fieldnames
                for row in reader:
                        rows.extend([{field[i]:row[field[i]] for i in range(len(field))}])
                with open(json_file,'w') as f:
                        f.write(json.dumps(rows,sort_keys=False, indent=4, separators=(',', ': ')))

csv_to_json('ff.csv','ff.json')

##read data from json file and print as a table
with open('cs_js.json') as jss:
        d = json.load(jss)
        dict = {}
        i = 0
        for median in d:
                if 'KEYWORD' in median:
                        if i not in dict:
                                dict[i] = median['KEYWORD']
                                i = i + 1
                        else:
                                continue
                else:
                        print("KEYWORD' does not exist in this JSON entry")

df = pd.DataFrame(dict,index=['INDEX1']).T)

##print dataframe in table format
print(df)

##plot dataframe as a line plot
ax = plt.gca()
df.plot(kind='line',x='index',y='KEYWORD',ax=ax)
