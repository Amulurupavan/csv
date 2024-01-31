import csv
fp=open('one.csv','r')
emp_data=list(csv.reader(fp))
print(emp_data)

for emp_row in emp_data:
    #print(emp_row)
    for word in emp_row:
        print(word,"\t", end="")
    print()
        
        
fp.close()