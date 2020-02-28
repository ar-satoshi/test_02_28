try:
    f=open("input.txt","r")
except IOError:
    print("file can't open")
    exit()
lines=f.readlines()
ls=[]

for i,line in enumerate(lines):
    ls.append(line.split(":"))
    ls[i][0]=int(ls[i][0])
"""
for l in ls:
    print(l)
"""
k=ls[i][0]

ls.sort()

#print(ls)

j=0
string=[]
flag=0
while j<i:
    if (k % ls[j][0]==0):
        string.append(ls[j][1])
        print(ls[j][1],end="")
        flag=1
    j+=1

if(flag==0):
    print(str(k))
