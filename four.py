import csv
fp=open('one.csv','r')
emp_data=list(csv.reader(fp))
#print(emp_data)
print(emp_data[2:])


fp.close()