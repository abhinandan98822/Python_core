# a=6
# b=9
# c=a+b
# print(c)

#if-elif-else statements

# a=int(input("enter first num="))
# b=int(input("enter second num="))
# if(a>=b):a=3
# b=4
# print(a is b)
# print(a is not b)

# a=[1,2,3,4,5,5,6]
# b=[1,2,3,4,5,5,6]
# print(a in b)
# print(a not in b)
# print(a==b)
#     print("a is greater than or equal to b")
# elif(a<=b):
#         print("a is less than or equal to b")
# else:
#     print("a is smaller than b")   


# #ladder if statement

# a=int(input("enter first num="))   
# b=int(input("enter second num="))
# if(a>b):
#     print("a is greater than b")
#     if(a<b):
#         print("a is less than b")
#         if(a==b):
#             print("a is equal to b")
#         else:
#             print("a is not equal to b")    
#     else:
#         print("a is not less than b")    
# else:
#     print("a is smaller than b")

#append value in the list
# a=[1,2,3,4,5,6]
# a.append(8)
# print(a)


#pop
# a=[1,2,3,4,5,6]
# a.pop(3)     #remove the third value from the list
# print(a)

# a=[1,2,3,4,5,6]
# a.remove(3)  #to remove the three from the list
# print(a)

#delete tuple
# a=(1,2,3,4,5,6)
# print(a)
# del a
# print(a)


#dictonery in python
# items={
#     "fruitname":"apple",
#     "VegName":"Carrot",
#     "fastfood":"Chowmin",
#     "JUICE":"sugarjuice"
# }
# print(items)


#accessing a element using a key in python
# from importlib.resources import Package


# items={
#     "fruitname":"apple",
#     "VegName":"Carrot",
#     "fastfood":"Chowmin",
#     "JUICE":"sugarjuice"
# }
# print(items["fruitname"])


#accessing a element inside element using a key in python

# items={1:{"fruitname":"apple","VegName":"Carrot","fastfood":"Chowmin","JUICE":"sugarjuice"},
# 2:{"breakfast":'bread','lunch':'Chawal','dinner':'chicken'}}
# print(items[1]["VegName"])

#set
# a=(1,2,3,3,3,4,4,4,1,2,5)
# c=set(a)   #set don't call duplicate elements
# print(c)

#identity Operator
# a=3
# b=4
# print(a is b)
# print(a is not b)

# a=[1,2,3,4,5,5,6]
# b=[1,2,3,4,5,5,6]
# print(a in b)
# print(a not in b)
# print(a==b)

#Changing the values of a and b with one another
# a=9
# b=6
# a=b
# b=a
# print(b)
# print(a)


#FOR__LOOP
# a=7
# for i in range(11):   #print the tale of 7
#       print(a,"*",i,"=",a*i)

#example-1:
# a=int(input("enter any first num="))
# b=int(input("enter second num="))
# if(a>b):        #use of if condition to print table
#  for i in range(11):
#      print(a,"*",i,"=",a*i)
# else:
#  print(a,"is smaller than",b,"so Table of",a,"is not printed")     

#example-2:
# for i in range(6):   #row         #triangle in increasing order
#     for j in range(i):   #column
#         print("*",end="")
#     print()   

#example-3

# n=8                               #triangle in decreasing order
# for row in range(n):
#     for column in range(n-row):   
#         print("*",end="")
#     print() 
# 
# example-4
# a=7
# for row in range(a):
#     for column in range(a):
#         print("*",end=" "
# 
# 
# are
#     print()   
# 

 #example-5
# a=int(input("enter any num="))
# for row in range(1,a+1):
#     print("*"*row)             #left triangle
 

#  example-6
# a=int(input("enter any num="))     #right tringle
# for row in range(1,a+1):
#   print(" "*(a-row)+"*"*row)


# example-7
# a=int(input("enter any num="))
# for i in range(1,a+1):
#     print(" "*(a-i)+"* "*i)     #complete triangle


#example-8
# a=int(input("enter any num="))
# for i in range(1,a+1):
#     print(" "*(a-i)+"* "*i)    #diamond shape
# for i in range(a,0,-1):
#     print(" "*(a-i)+"* "*i)


#example-9
# a=int(input("enter any num="))
# for i in range(a,0,-1):     #Opposite triangle
#     print(" "*(a-i)+"* "*i)

#example-10
# a=int(input("enter any num="))
# for i in range(a,0,-1):
#print("space"*(value-iteration)+"*"iteration)
    # print("  "*(a-i)+"* "*i)      #right opposite triangle

#break-continue-pass
# a=int(input("enter any num="))
# for i in range(1,10):
#     mynum=a+1
#     if (mynum<5):
#         print(a+i) 
#         break   
#     else:
#         print("not defined")  

# a=int(input("enter any num="))
# for i in range(10): 
#     x=7
#     if(a>x):
#         print(a+i)      
#         continue 
#     else:
#         print("not defined")    
#         break       #use break to print else condition once in loop when it false

#while-loop
# a=9
# while(a<11):
#     print(a)
#     a+=1

#functions
# def add(a,b):
#  c=a+b            #add function
#  print(c)
# add(1,2)


# def add():
#     num1=int(input("enter first num="))
#     num2=int(input("enter second num="))    #add function
#     total=num1+num2
#     print(total)
# a=add()  

# def subtract():
#     num1=int(input("enter first num="))
#     num2=int(input("enter second num"))    #subtract  function
#     print(num1-num2)
# subtract()    

# def multiply():
#     num1=int(input("enter first num="))
#     num2=int(input("enter second num="))    #multiply function
#     print(num1*num2)
# multiply()

# def divide():
#     num1=int(input("enter my first num"))
#     num2=int(input("enter second num"))     divide function
#     print(num1/num2)
# divide()    


#####call function one by one#########

# num1=int(input("enter first num="))   #global variale
# num2=int(input("enter second num="))
# def add(a,b):
#     total=a+b
#     print(total)
# add(num1,num2)

# def subtract(a,b):
#     total=a-b
#     print(total)
# subtract(num1,num2)   

# def multiply(a,b):
#     total=a*b
#     print(total)
# multiply(num1,num2) 

# def divide(a,b):
#     total=a/b
#     print(total)
# divide(num1,num2)    

#Enter table inside functions according tom loop

# num1=int(input("enter first num="))
# num2=int(input("enter second num="))
# def function(a,b):
#     for i in range(11):
#         if(a>b):
#          print(a,"*",i,"=",a*i)
#         else:
#             print(a,"when iteration=",i) 
            
# function(num1,num2)            


#condition to find odd even inside one loop
# for i in range(100):
#     if(i%2!=0):
#         print("The odd num is=",i)
    
#     elif(i%2==0):
#         print("the even num is=",i)
    
#     else:
#         print("not defined")    
    
#condition to find odd num and even num continuosly
# for i in range(100):
#     if(i%2!=0):
#         print("the odd num is=",i)    

# for i in range(100):
#     if(i%2==0):
#         print("the even num is=",i)   


#print odd even inside one loop
# for i in range(100):
#     if(i%2!=0):
#         print('odd num=',i)   #check odd even in one loop (nested for if loop)
#     if (i==100):
#         for i in range(100):
#             if(i%2==0):
#                 print("even num=",i)

#Recursion
# def function():
#     a=6
#     print(a)
#     function()    #
# def function(a,c):
#     c+=2
#     a+
#     if(a+c<19):
#         return
#     print(c) 
#     function()   
# function(1,2)   #function call itself upto the particular limit
# # function()    


#factorial__
# def fac_iteration(n):   # n is integer
#     fac=1
#     for i in range(n):
#         fac=fac*(i+1) 
#     return fac    
# pass
# num=int(input("enter any num=")) 
# print(fac_iteration(num)) 

#lamda function
# from logging import exception


# num=lambda x,y,z:x+y+z   
# print(num(1,2,3))

# n=lambda x,y,z:x-y-z
# print(n(6,7,8))

#exception handling

# a=[6,7,8]
# try:
#    print(a[3])

# except Exception as name:  
#     print(name)  

# finally:
#     print("this is final block")

















                                             
    

