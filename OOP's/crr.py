#pyhton variales
#local
# def student():
#     a=10
#     b=6
#     return a+b
# c=student()
# print(c)

#global
# c=7
# def student():
#     a=4
#     b=9
#     return a*b*c
# res=student()   
# print(res)

#convert tuple into set
# b=(1,2,3,4,5,5,6,7,7,8,8)   #duplicate values repeats
# print(set(b))

# #convert set into tuple
# b=(1,2,3,4,5,5,6,7,7,8,8)   #duplicate values are not repeats
# print(set(b))

# #append
# b=[1,2,3,4,5]   #append does'nt use in tuple
# b.append(6)
# print(b)

#pop
# b=[1,2,3,4,5,6,7]
# c=b.pop(3)
# print(c)

#remove
# a=[1,2,3,4,5,6]
# c=a.remove(4)
# print(c)

#delete
# a=[1,2,3,4,5]
# print(a)
# del a
# print (a)


# control flow statemets
# if-else
# a=int(input("Enter num-"))
# b=int(input("Enter num-"))
# if(a>b):
#     print("a is greater than b")
# else:
#     print("b is greater than a")   


#nested if-elif-else statement
# a=int(input("Enter num-"))
# b=int(input("Enter num-"))
# if(a>b):
#     print("a is greater than b")
# elif(a<b):
#     print("a is smaller than b")    
# else:
#     print("else block run")   

#nested if statement
# a=int(input("Enter num-"))
# b=int(input("Enter num-"))
# if(a>b):
#     print("a is greater")
#     if(a<b):
#         print("a is smaller")
#         if (a==b):
#             print("a is equal equal to b")
#         else:
#             print("3rd if block")    
#     else:
#         print("2nd if block")
# else:
#     print("3rd if block")                


#for---loop
# a=[1,2,3,4,5]
# for i in  a:
#     print(i)


# for i in range(100):
#     if(i%2==0):
#         print("even num=",i)
#     elif(i%2!=0):
#         print("odd num=",i)       #odd and even no. continusly
#     else:
#         print("done")    


# for i in range(100):
#     if(i%2==0):
#         print("even num=",i)    #nested loop
#     if(i==98):
#         for i in range(100):
#            if(i%2!=0):
#             print("odd num=",i)      
# 

#print tables
# a=int(input("enter num="))
# for i in range(11):
#     print(a,"*",i,"=",a*i) 

# for i in range(1,7):  #left side of triangle
#     print("*"*i)  

# a=8
# for row in range(1,7):
#    print(" "*(a-row)+"*"*row)

a=int(input("enter num="))     #print square
for row in range(a):
    print("*"*row)

  



 
   
