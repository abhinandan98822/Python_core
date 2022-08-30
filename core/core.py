#___________________________________P--Y--T--H--O--N____C--O--R--E______________________________________________________

# python variables
# a=8
# v=9
# j=a+v
# print(j)

#local_variables
# def function():
#     local="local"
#     print('local')
# function()


#Global_variable/local
# a=4    #local variable
# def goal():
#     a=6
#     b=8 #global variable
#     c=a+b
#     print(c)
# goal()
# print(a)

# use of eval
# num=eval(input("enter any numbers-"))
# print(num)   #eval is directly evaluate numers in terminal

#changing numbers with one another
# a=6
# b=7
# a,b=b,a
# print(a,b)

#delete function
# a=3
# print(a)
# del a
# print(a)

#type of variables in python
#1)local-define only inside the function
#2)gloal-define  oth inside or outside the function


# #local variable
# def function():
#     x="local_function"
#     print(x)
# function()
#
# #global variables
# x="global_function"
# def fun():
#
#  print("x inside-",x)
# fun()
# print("x outside-:",x)
#
# #datatypes in python
# # 1)integer-int,float,complex
# # 2)sequence-list,tuple,string
# # 3)Boolean-True,false
# # 4)set
# # 6)dictonery
#
# # 1)
# # a=34
# # b=23.5
# # c=4+2j    #in python complex datatype only take"j" alphabet
# # print(a+b+c)
#
# # 2)Tuple-it is umutable--means the elements of tuple cannot e changed
# x=(1,2,3,4,5,6)
# print(type(x))
# print(x[1:3])
#
# x=(1,)  # , is used for given braces to the tuple
# print(x)
#
# # list-mutable--means the elements of list can be changed
# x=(1,2,3,4,5)
# print(type(x))
# print(x[:4])
#
# #methods of list in python
# #remove
# a=[1,2,3,4,5]
# a.remove(4)
# print(a)
#
# #append
# a=[1,2,3,4,5]
# a.append(6)      #add the element at the end of the list
# print(a)

#insert
# a=[1,2,3,4,5]
# a.insert(2,8)     #insert the element at given position of the list
# print(a)

#pop
# a=[1,2,3,45]
# a.pop(3)    #pop function remove element on the basis of index number/or slicing
# print(a)
#
# #sort
# a=[2,3,2,62,47,3]
# a.sort()  #sort is used to arrange the elements in systematic order
# print(a)
#
# #reverse
# a=[2,3,2,62,47,3]
# a.reverse()  #print the list in reverse order
# print(a)

#slicing
# a=[1,2,3,4,5,6,8]
# print(a[0:5])
#
# #extended slicing
# a=[1,2,3,4,5,6,8]
# print(a[0:5:2])   #given the gap of 2
# print(a[::2])     #given the gap of 2
# print(a[:-1])     #minuse the last digit of the list
# print(a[::-2])    #start the list from opposite side with the gap of 2



#string
# a="akshay"
# b="abhinandan"
# print(type(a+b))
# print("the name of both boys are",a + b)
#
# 3)Boolean
# a=6
# b=7
# print(a==b)
# or
# a=5
# b=5
# print(a==b)

#4)set
# set={1,2,2,3,4,4,5,6,"abhi",56.8}
# print(type(set))
# print(set)
#add value to the set
# set.add(9)                #only on evalue add once
# print(set)

#remove value from the set
# set.remove(4)   #only one value remove at once
# print(set)

# 5)Dictonery
# dict={"name":"abhi","class":"CA",1:"56"}
# print(dict)
# print("the name is-"+dict["name"]+''+dict[1])
# print("the class is"+dict["class"])
#

######################------------------OPERATOR------------------#############
# # Airthmatic_operator
# a=5
# b=87
# c=a+b,a-b,a*b,a/b,a//b,a**b
# print(c)
#
# #assignment operator
# a=6
# a+=5
# a-=3
# a*=2
# a//=2
# a%=3
# print(a)
#
#
# #comparison operator
# a=6
# c=5
# print(a==c)
# print(a>c)
# print(a<c)
# print(a!=c)
# print(a<=c)
# print(a>=c)
#
# #Bitwise_opertor
#
# # _____AND Operator
# a=5
# b=4
# c=7
# print(a&b)
# print(c&a)
# print(c&b)
#
# print(a and b)
# print(c and a)                   #  and only takes second number
# print(c and b)
#
#
# #_____OR Operator
# a=5
# b=6
# c=7
# print(a|b)
# print(a|c)
# print(b|c)
#
# print(a or b)
# print(a or c)      #or only takes first number
# print(b or c)
#
# #not operator
# a=5
# b=6
# c=7
# print(a^b)
# print(a^c)
#
# #Nor operator/complement operator
# a=5
# b=6
# c=9
# print(~a,~b,~c)
#
# #left-shift operator
# a=6
# b=2
# print(a<<b)   #shift the bits from the right sid eof operator
#
# #Right-side Operator
# a=7
# b=3
# print(a>>b)    #shift the bits into right sid eof operator

#identity_Operator
#Check whether the value is same or not
#there are two types of identity operator

# 1)Is Identity operator

# a=5
# b=9
# print(a is b)

#2) Is-not identity Operator
# a=5
# b=9
# print(a is not b)


#_____________CONTROL FLOW STATEMEMTS______________

#CONDITIONAL STATEMENTS
# 1)IF
# 2)IF_ELSE
# 3)IF_ELIF_ELSE
# 4)nested-if-else


#If_condition
# a=6
# b=8
# if(a!=b):
#     print("Condition is true")
#
# #
# #If_ELSE condition
# a=7
#
# if(a<=4):
#     print("condition is false")
# else:
#     print("condition is true")
#
#
# #IF_ELIF_ELSE condition
# a=7
# if(a>=9):
#     print("wrong answer")
# elif(a<9):
#     print("elif condition runs")
# elif(a==7):
#     print("number is equal")
# else:
#     print("condition not defined")


#Nested If-else Condition
# num1=int(input("enter first number="))
# num2=int(input("enter second number="))
#
# if(num1==num2):
#     print("first if condition runs")
# elif(num1>num2):
#         print("elif condition runs")
#         if(num1>=num2):
#             print("2nd if condition runs")
#             if(num1<=num2):
#                 print("3rd if condition runs")
#             else:
#                 print("3rd if condition else part runs")
#         else:
#             print("2nd else part runs of if condition")
# else:
#     print("else part of first if condition")


#Loops
# 1)For_LOOP

#example-1
# a=10
# for i in range(a):
#     print(i,end=" ")  #end is used to print in one row
#
#
# #example-2
# name1="Abhinandan"
# name2="Akshay"        #print name1 10 times and name2 11th time
# for i in range(11):
#      if (i<10):
#          print(name1)
#      else:
#          print(name2)
#

# #example-3
# array=[1,2,3,4,5]
# sum=0
# for i in range(len(array)):
#  sum=sum+array[i]
# print("sum of all the elements of array=",sum)
#
# #example-4
# array1=[1,2,3,4,5]
# array2=[1,2,3,4,5]
# sum=0                  #sum is taken to store both arrays because one empty variale needs to store values
# for i in range(5):
#  sum+= array1[i] + array2[i]
# print("the sum of both array are",sum)
#

# #example-5
# print("multiplication table")
# for i in range(8,11):
#     for j in range(1,11):      #print table using for loop
#         print(i,"*",j,"=",i*j)
# #     print(" ")
# #

# #example-6
# a=5
# for i in range(a):
#     for j in range(0,11):
#         print(i,"*",j,"=",i*j)
#     print("")
#

# #example-7
# a=int(input("enter any numer for table="))
# for i in range(1,a,3):
#     for j in range(0,11):
#         print(i,"*",j,"=",i*j)
#         print("")


#example-8
# list=["apple","mango","pear","orange"]
# for i in list:
#     print(i)
#     print(i[2])


#example-9
# print_pattens using for loop in python
# num=int(input("enter the num of row="))      #left triangle
# for i in range(1,num):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()


#example-10
#print square using for loop
# value=int(input("enter any number-"))
# for rows in range(value):
#     for columns in range(value):
#         print("*", end=' ')  #this end is for giving space between columns
#     print()


#example-11
#print increasing tringle pattern/nested for__loop
# n=6
# for row in range(n):
#     for columns in range(row+1):
#         print("*",end=" ")
#     print()

#decreasing triangle pattern
# n=6
# for row in range(n):
#     for column in range(n-row):
#         print("*",end=" ")
#     print()


#using transfer statements in for-loop
# 1)break
# 2)Continue
# 3)pass

#break
# num=int(input("enter any number="))
# for i in range(1,10):
#     mynum=num+1
#     if (mynum<10):
#         print(i+num)
#         break
#     else:
#         print("not defined")

#continue
# num=int(input("enter any number="))
# for i in range(1,10):
#     mynum=num+1
#     if (mynum<10):
#         print(i+num)
#         continue
#     else:
#         print("not defined")

#pass
# num=int(input("enter any number="))
# for i in range(1,10):
#     if (num>10):
#         print(i+num)
#         pass
#     else:
#         print("not defined")

#______While__Loop
# i=5
# while i<9:
#     print(i)
#     i=i+1

#break_statement in while loop
# i=0
# while i<8:
#     print(i)       #when the value of the loop becomes 3 it will automatically stops
#     i+=1
#     if (i==3):
#       break

# #continue statement in while loop___
# i=0
# while i<8:
#    i +=1
#    if (i==6):
#       continue
#    print(i)
#
#pass statement in while loop___
# x=int(input("enter first num-"))
# y=int(input("enter second num-"))
# total=x+y
# while total<20:
#     total+=1
#     print(total)

#Functions in python____

# def function():
#     print("Hello")
#     print("Myname is Abhinandan")
# function()  #---1    number of times you call the function it will printed
# function()  #---2


#example-1
#pass parameter/argument to the function
# def function(Name):  #argument/parameter
#     print("Hello",Name)
#     print("This is Morning")
# function("Abhinandan")     #pass value

#example-2
#function to add numbers
# def function(a,b):
#     total=a+b
#     print("sum of num=",total)
# function(6,7)

#example-3
#use of "return" in function
# def function(a,b):
#     total=a+b
#     return total
# print(function(6,7))

#example-4
# def function(name,age):
#     return "the Name is",name,"and age is",age
# name="Abhinandan"
# age=23
#value=function(name,age)
# print(value)

#built in function
#example-1
# num=(1,2,3,4,5)
# length=len(num)
# print("The length of num is",length)

#example-2
# num=[1,2,3,4]
# sum=sum(num)
# print("The sum of num is",sum)

#example-3
#Q)-Write a function to create the average marks and grade in university

#function to find the average marks
# def find_average_marks(marks):
#  sum_of_marks=sum(marks)       #total sum of marks
#  num_of_subjects=len(marks)     #total num of objects
#  average_marks=sum_of_marks/num_of_subjects    #to find average marks
#  return average_marks

# #function to find grade
# def find_grade(average_marks):
#     """ This function is second function to find grade"""
#     if average_marks>=80:
#         return "grade_A"
#     elif average_marks>=60:
#         return "grade_B"
#     else:
#         return"fail"

#call function for marks
# marks=[55,65,75,90,40]
# average_marks=find_average_marks(marks)    #save function in variable
# print(average_marks)   #print variale where we store function value
# #
# #call function for grade
# # grade=find_grade(average_marks)      #call grade function
# # print(grade)


#types of arguments in functions
# 1)default arguments-in dflt argument value is already given to the arguments
# 2)keyword arguments-pass the  value with variale name
# 3)variable-length argument    -pass the variables in different numbers of arguments in diff. function

# #default argument
# def default(x=2,y=5):  #value already given inside the arguments
#     z=x+y
#     print(z)
# default()


#keyword arguments
# def keyword(x,y):
#   z=x+y
#   print(z)
# keyword(x=3,y=9)   #pass the value with variale name

#variable_length_argument
# def variable_length(*x):  #we use "*" which is called pointer
#     for i in x:     #i carry the different values which we can store in x
#      print(i)
# variable_length(1,2,3,4)
# variable_length("Abhinadan")    #variable_length_argument is pass diff numbers of arguments in single variable
# variable_length(23.5)


#RECURSION-Python also accept function recursion means recursion function can call by itself.
# i = 1
# def factorial(a,i):
#     if i == a:
#         return "true"
#     s = a *i
#     print(s)
#     i += 1
#     run=factorial(4,i)   #run is declared inside the function
#     factorial(run)        #so function is declared inside because variable is call inside the function

#example-2
# def greet(a):
#     print("hello")
#     greet()              #function call by itself
# greet()

# example-3
#iterative_function
# """
# n!=n * n-1 *n-2 * n-3.....
# n!-n*(n-1)!
# """
# def factorial_iterative(n):
#     """
#      :param n: Integer
#     :return:n * n-1 * n-2 * n-3.....!
#     """
    # fac=1
    # for i in range(n):
    #     fac=fac *  (i+1)
    # return fac
    # pass
# number=int(input("enter any number="))
# print(factorial_iterative(number))

# example-3

# def factorial_recursive(n):
#     if n==1:
#         return 1
#     else:
#         return n * factorial_recursive(n-1)
# number=int(input("enter any number="))
# print(factorial_recursive(number))

#Lambda function in python
# def add(a,b):
#    return a+b
# minus=lambda x,y:x-y  #lambda is not a function but works as same as function
#            #both ab

# both lambda and function minus are doing same work
        #def minus(x,y)
         # return x-y
# print(minus(9,4))

#EXCEPTION HANDLING
# 1)Built-in-exception
# 2)User-defined-

#try:-- is is used for code block where you think exception may e occurs
#except:--Except block may catch the exception of try lock. in one try block there are multiple numbers of exception
#else:--this lock may executed when no exception is raised in try block.
#finally:--this block may execauted in any condition if there is exception in code or not.

#example-1
# a=8
# b=2
# try:
#     c=a/b
#     print(c)
# except Exception as name:   #this is used to get exception
#      print(name)
# else:
#     print("Their are no error in try lock so code exeauted")
# finally:
#     print("so program execauted")






























































