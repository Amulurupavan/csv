import csv
fp=open('one.csv','r')
user_data=list(csv.reader(fp))
print(user_data)


    
for emp_row in user_data:
    #print(emp_row)
       
    for word in emp_row:
        print(word[1:],"\t",end="")
        
        print()
        fp.close()