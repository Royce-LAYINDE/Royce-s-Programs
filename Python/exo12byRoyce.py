n=input("entre des nombres séparés par un @  ")
l=[]
l.append(n)
for i in l:
    li=i.split("@")
li=list(map(int,li))
li.sort(reverse=True)

print(li)


