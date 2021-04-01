row_col_num  = int(input("How many rows and columns do you want to creat enter number: "))
li =[]

for i in range(row_col_num):
    l = []
    for j in range(row_col_num):
         l.append(int(input("enter number")))
    li.append(l)

for i in range(len(li)):
    for j in li:
        
        
