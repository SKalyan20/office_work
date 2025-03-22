import csv
from openpyxl import load_workbook

wb=load_workbook(filename='C:/Users/oper/Downloads/book3.xlsx')
sheet=wb.active
csv_data=[]
for value in sheet.iter_rows(values_only=True):
    csv_data.append(list(value))
    
with open('sampledata.csv','w')  as csv_obj:
    writer=csv.writer(csv_obj,delimiter=',')
    for line in csv_data:
        writer.writerow(line)
