# a=[1,2,3]
# =INT(RAND()*1000)

# a[0]= 3

# # for i in range(0,10):
# #     print(i)
# x=0
# y=0
# ho=[9,8,7,6,5,4,3,2,1,0]
# print(ho[1])
# for i in range(0,9):
#     if ho[i] > ho[i+1]:
#         y=ho[i] 
#         x=ho[i+1]
#     else:
#         x=ho[i] 
#         y=ho[i+1]
#     ho[i]=x 
#     ho[i+1]=y 
# print(ho)

# i=0
# print("%d"%(i+1))
# print("I ate {number} apples. so I was sick for {day} days.".format(day=3,number=10))


# ho=[9,4,2,6,0,7,8,1,11,99]
# for i in range(1,10):
#     for j in range(0,i):
#         if ho[i-j+1]<ho[i-j]:
#             ho[i+1-j],ho[i-j]=ho[i-j],ho[i+1-j]
        

ho=[4,2,3,1]
for i in range(0,3):
    for j in range(0,i+1):
        if ho[i-j+1]<ho[i-j]:
            ho[i+1-j],ho[i-j]=ho[i-j],ho[i+1-j]
        else: break
print(ho)