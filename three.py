import csv
fp=open('one.csv','r')

emp_data=list(csv.reader(fp))
new_emp_data=emp_data[0:]
print(type(new_emp_data))

#print all emp id 
for emp_list in new_emp_data:
    i=0
    while i<=len(emp_list)-1:
        print(emp_list[0])
        i=i+1

    



fp.close()