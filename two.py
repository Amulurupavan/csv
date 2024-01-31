import csv
fp=open('one.csv','r')
emp_data=list(csv.reader(fp))
print(type(emp_data))

#print all emp ids.

for emp_row in emp_data:
    #print(emp_row[0])
    i=0
    while i<=0:
        print(emp_row[0])
        i=i+1
        
        
        
fp.close()