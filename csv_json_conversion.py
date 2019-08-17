#json to csv and csv to json

import urllib,json
import requests
import csv

##json to csv
def json_to_csv(jsonf,csvf):
    response = urllib.request.urlopen(jsonf)
    data = json.loads(str(response.read().decode("utf-8")))
    csv_columns = ["COLUMNS IN YOUR JSON FILE"]
    try:
        with open(csvf, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for lines in data:
                writer.writerow(lines)
    except IOError:
        print("I/O error")

json_to_csv(jsonfile_name,csvfile_name)

##csv to json
def csv_to_json(csvf,jsonf):
        rows = []
        with open(csvf) as csvfile:
                reader = csv.DictReader(csvfile)
                field = reader.fieldnames
                for row in reader:
                        rows.extend([{field[i]:row[field[i]] for i in range(len(field))}])
                with open(jsonf,'w') as f:
                        f.write(json.dumps(rows,sort_keys=False, indent=4, separators=(',', ': ')))

csv_to_json(csvfile_name,jsonfile_name)
