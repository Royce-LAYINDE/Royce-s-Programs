f = open("E:\\DATA\\Python\\dataset.txt") 
lst=[]
lst1=[]
lst2=[]
for line in f.readlines():
    a=line.strip("\n").split("\t")
    #print(a)
    
    
    
    
    for i in a:
        b=i.split(",")
        b=str(b)
        c=b.strip("['")
        d=c.strip("']")
        #print(d)
        
            
        lst.append(d)
for i,e in enumerate(lst):
    if i%2==0:
        lst1.append(e)
    else:
        lst2.append(e)
print(lst1)
print(lst2)
        
        
        #lst.append(i[0])
        #lstx.append(i[1])
#print(lst)
        
                
            
