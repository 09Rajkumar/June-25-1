import csv
import pandas as pd
with open("test.csv","r") as op:
    rf = csv.reader(op)
    ls = []
    for row in rf:
        if len(row) != 0:
            ls = ls + [row]
op.close()
df = pd.DataFrame(ls)
print(df)
