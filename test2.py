a=[1,2,3]

a[0]= 3

# for i in range(0,10):
#     print(i)
x=0
y=0
ho=[9,8,7,6,5,4,3,2,1,0]
print(ho[1])
for i in range(0,9):
    if ho[i] > ho[i+1]:
        y=ho[i] 
        x=ho[i+1]
    else:
        x=ho[i] 
        y=ho[i+1]
    ho[i]=x 
    ho[i+1]=y 
print(ho)

i=0
print("%d"%(i+1))