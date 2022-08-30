#=========================================================================================
#|------=----=--=--=-------------------OOP'S---------=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|
# =========================================================================================

#four principles of oop's
# 1)object--object is an instance of class
# 2)class--Class is a blueprint
# 3)Inheritance
# 4)Polymorphism
# 5)Encapsulation
# 6)Abstraction

#create classes___class vs. Instance___
# example-1

#class
# class Software_Eng:    

# #oject
#    def __init__(self,name,age,salary,position): 

#         #instance/object attriutes
#         self.name=name
#         self.age=age
#         self.salary=salary
#         self.position=position

# #instance
# SE1=Software_Eng("Abhinandan",22,25000,"Designer")
# print(SE1.name,SE1.age)


#example-2
#print class attriute and object attriute
#class
# class Software_Eng:
 #class attriutes
    # company="CS_Infotech"

    # def __init__(self,name,age,salary,position):  #__init__method
        #instance attriutes
        #   self.name=name
        #   self.age=age
        #   self.salary=salary
        #   self.position=position
#instance
# soft_eng=Software_Eng("Abhinandan",23,24000,"Developer")    
# print(soft_eng.name,soft_eng.age,soft_eng.salary,soft_eng.position)   
# print(soft_eng.company)  #print class attriute--1
# print(Software_Eng.company)  #print class attriute--2


#RECAP
# 1)Class-blueprint
# 2)object-Instance and its attriute(function)
# 3)class vs Instace
# 4)Instance Attribute:define in __init__(self)
# 5)class Attributes:outside the Instance/object


# ___________________________________________________________________#
# student1=["Abhinandan","BCA",23,24000]   #global variables
# student2=["Akshay","BCom",28,27000]

# #Global__Function 
# def student(std):

#     print(f"{std[1]} is writing a code...")

# student(student1)   
#_______________________________________________________________________# 
#example-3

#Function inside class/print 2 objects attriutes at one time

#class
class Software_Eng:
#  class attriutes
    company="CS_Infotech"   #global variable

    def __init__(self,name,age,salary,position):  #__init__method   #first function
        # instance attriutes
          self.name=name
          self.age=age
          self.salary=salary
          self.position=position

    def function(self):       #second function
        print(f"{self.name} is writing a code...")   #instance method   

    def language(self,language):       #third function
        print(f"{self.name} is writing a code in {language}")  

        #___#__#__
        #instance_method
    def information(self):       #fourth function
        # making  __dict__ 
        information=f"name={self.name},age={self.age},salary={self.salary},position={self.position}"  
        return information 

#to print the string like method above"Instance Method"/dunder method
    def  __str__(self) :          #fifth function
        information=f"name={self.name},age={self.age},salary={self.salary},position={self.position}"  
        return information 

#check the equality of values we  pass to instance of class
    def __eq__(self, other):     #sixth function
        return self.age==other.name and self.age==other.age    
      
#function-6--use of condition inside class
    @staticmethod   #decorator to print function by instance name
    def entry_sal(age):
        if age<25:
            return 5000
        if age>30:
            return 10000        
# instance
soft_eng1=Software_Eng("Abhinandan",23,24000,"Developer") 
soft_eng2=Software_Eng("Akshay",23,26000,"Designer") 
soft_eng3=Software_Eng("Akshay",23,26000,"Designer")   #check equality  

print(soft_eng1.name,soft_eng1.age,soft_eng1.salary,soft_eng1.position)   
print(soft_eng1.company)  #print class attriute--1   #first function
print(Software_Eng.company)  #print class attriute--2

soft_eng1.function()   #call second function--first instance--attributes
soft_eng2.function()   #call second function--first instance--attributes

soft_eng1.language("python")    #call third function---attributes
soft_eng2.language("php")    #call third function---attributes

# call __dict__
print(soft_eng1.information()) #fourth function
print(soft_eng2.information())

print(soft_eng1)   #fifth function

print(soft_eng2==soft_eng3)   #sixth function

print(soft_eng1.entry_sal(32)) #seventh function
print(Software_Eng.entry_sal(24))   #call by class name   #seventh function

