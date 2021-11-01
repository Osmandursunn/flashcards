import csv
import pandas as pd
with open('nl.csv','w',encoding='UTF8') as csv_f:
    writer = csv.writer(csv_f)
    with open('nl.txt','r') as f:
        lines = f.readlines()
        for i in lines:
            i=i.split(' ')
            for k in i[0]:
                if k in '.':
                    i[0]=i[0].replace('.','')
            for k in i[1]:
                if k in '\n':
                    i[1]=int(i[1].replace('\n',''))
            writer.writerow(i)
data=pd.read_csv('nl.csv',header=None)
data_c = data.sort_values(by=[1], ascending=False)
data_c=data_c.iloc[:5000]
data_c[0].to_csv('nl_words_sorted.csv',encoding='utf-8',index=False,header=False)