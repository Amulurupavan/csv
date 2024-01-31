import csv
fp=open('one.csv','r')
user_data=csv.reader(fp)
user_list=list(user_data)
print("No of users:",len(user_list)-1)

i=0
while i<=0:
    print("no of users:",len(user_list)-1)
    i=i+1

fp.close()