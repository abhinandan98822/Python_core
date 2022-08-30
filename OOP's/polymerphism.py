#                               _____________POLYMERPHISM________________
"""Polymerphism-means Many Forms
                                 same name but doing different tasks"""

"""Methods in Polymerphism
1)Overriding-Methods with same name but doing different tasks
for eg. --we have a function of same same name but in different classes

2)Overloading-
""" 



#Example-1
#Overriding--


# class Parent:
    # student="Abhinandan"

# class Child(Parent):
    # #student="Akshay"  
    # pass

# Obj=Child()     #call class
# print(Obj.student) #call child class

#If the chile class doesn't have any object than it will directly calls parent class oject

# print(Obj.student) #call parent class 

#Example-2
# class Bank:      #main class
#     def interest():
#         return 5
        


# class PNB(Bank):     #sub class
    # def interest():
        # return 10.7
        # pass
     

             
# obj=PNB()
# print(PNB.interest())

#if subclass method is not availale than it will call the parent class method 


#Method overloading
# 1)In python we can define a method In such a way that you can call it multiple times.

#example-1#based on the parameters the behaviour is changed
# class student:
#     def first_name(self,name=None):  #method
#         if name is not None:
#             print("Hello",name)
#         else:
#             print("Hello") 

# oj=student()
# print(oj.first_name("Akshay"))      #We call name here so it will print if statement 
# print(oj.first_name())         #name is not passed so here will return only else condition

