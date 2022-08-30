#example-2
# class student:

#     def function(a,c):
#        return a+c
   
# a=student.function(1,2)   
# print(a)     

#call class using function
# class student:

#     def __init__(self,name,age,mobile):
#         self.name=name
#         self.age=age
#         self.mobile=mobile

# std=student('Abhinadan',23,9882233239)   
# print(std.name,std.age,std.mobile)
    
# class Student:
                      
#      def function():
#         person={'name':'Abhinandan','age':23,'mobile':9882233239} 
#         return person

# #call dictonery ojects inside function of objects without giving the parameters
# x=Student.function()
# print(x['name'])

#use of if condition inside function          
# class Sum:

    # def add():
    #     a=int(input("enter first num="))     
    #     b=int(input("enter second num="))   
        # if (a<b):
        #     return'a is smaller than b'
        # else:
        #     return'a is greater than b'  

# result=Sum.add() 
# print(result)  

# result=Sum.add()      #class call again and again
# print(result)  


#print global values inside class
# class college:
#     all_students=300
#     def __init__(self,BCA,BBA,MBA):
#         self.C1=BCA
#         self.C2=BBA
#         self.C3=MBA
    

# result=college(100,150,200) 
# total1=result.all_students-result.C1
# total2=result.all_students-result.C2
# total3=result.all_students-result.C3
# print("Total _students=",result.all_students,'\n'," no. of Std in BCA=",'\n',result.C1,"left students=",total1,'\v')
# print("Total _students=",result.all_students,'\n'," no. of Std in BCA=",'\n',result.C2,"left students=",total2,'\v') 
# print("Total _students=",result.all_students,'\n',"no. of Std in BCA=",result.C3,'\n',"left students=",total3,'\v') 


#example--
# from unicodedata import name

# from paramiko import Agent


#Call global class variable
# class employee():
#     name="Akshay"

#     def __init__(self,name,age,salary) -> None:
#         self.name=name
#         self.age=age
#         self.salary=salary



# values=employee('Abhinandan',22,14000)
# print(values.name,values.age,values.salary)
# print(employee.name)



#_______________________________________________________________________#
#class and its instance

# se1={"software_eng","Akshay",23,"chemistry"}
# se2={"software_eng","Abhinandan",24,"physics"}

#class
# class software_eng:
#     tech='Anita'    #global attribute is call by inside function or outsid the function
#     def __init__(self,name,age,subject):
#         self.name=name
#         self.age=age
#         self.subject=subject

# #instance
# se1=software_eng("Akshay",23,"chemistry") 
# se2=software_eng('Abhi',34,'Physics') 
# print(f"The name is {se1.name},The age is {se1.age},and the Subject is {se1.subject},and the teacher is {se1.tech}")  
# print(f"The name is {se2.name},The age is {se2.age},and the Subject is {se2.subject},and the teacher is {se2.tech}") 

#recap
# 1)class bluprint
# 2)instance of class
# 3)instance attributes defines indie the __init__(self)

#___________________________________________________________________
#global function

#example-1
# se1=["software_eng","Akshay",23,"chemistry"]
# se2=["software_eng","Abhinandan",24,"physics"]

# def code(per):
  
#     print(f"{per[1]} is writing a code")  #pass variable to the function
#   #note--indexing can e done into the array
# code(se1) 
# code(se2)

#example-2
# def code1(age):

#   #indexing can done only in the array
#     print(f"{age[1]} years old")

#     print(f"{age[1]}is  my name and the age is {age[2]} and the subject is {age[3]} i am a {age[0]}")


# code1(se1)    
# code1(se2)

#__________________________________________________________________________________________
#instance method

# class Student:
#     def __init__(self,name,subject,age) :
        
#        self.name=name
#        self.subject=subject
#        self.age=age

# #instance method
#     def std(self):
#         print(f"{self.name} is writing")
#         print(f"{self.age} is years old")
#         print(f"{self.subject} is major")
        


# #instance
# se1=Student("Abhinandan","BCA","24")
# se2=Student("Akshay","MCA","26")


#  #call instance method
# se1.std()
# se2.std()      #we don't pass parameter here it self automatically takes from variales

                #_________________________________________________
#instance method,pass functions

# class Student:
#     def __init__(self,name,subject,age) :
        
#        self.name=name
#        self.subject=subject
#        self.age=age


  #instance method call multiple parameters
    # def language(self,language):   #pass parameter inside
    #     print(f"{self.name} is singing in language{ language}")    #function-2
        


#instance
# se1=Student("Abhinandan","BCA","24")
# se2=Student("Akshay","MCA","26")


 #call instance method
 #we don't pass parameter here it self automatically takes from variales

# se1.language('hindi')
# se2.language('English')

#_________________________________________________________________________________
#return values from the function using return
# class Student:
#     def __init__(self,name,age,place):
#         self.name=name
#         self.age=age
#         self.place=place

#     def function(self):
#         information=f"name={self.name},age={self.age},place={self.place}"
#         return information 

# std1=Student("Abhinandan",23,"Mohali")
# std2=Student("Akshay",24,"Chandigarh")
# print(std1.function())  

#____________________use __str__ to return instance directlt without calling function

#dunder method
# class Cars:
#     def __init__(self,Car,model,price):
#         self.name=Car
#         self.model=model
#         self.price=price
        
        
#   __str__ for directlt call func
#     def __str__(self):
#         information=f"Car={self.name},model={self.model},price={self.price}"
#         return information

#   use __eq__ to compare the value of fucntion
#     def __eq__(self,other):
#         return self.name==other.name,self.model==other.model

#     def model(price):                     #use of if-condition_

#         if price<50000:
#             return"price is less"
#         if price>50000:
#             return"price is more"
#         else:
#             return"not defined"    


# car1=Cars('Maruti',2012,'2lakh') 
# car2=Cars("verna",2015,40000)   #use Cars.car because __init__doesn't define above 
# car3=Cars("verna",2015,40000)



# print(car1)
# print(car2)
# print(car2.name==car3.name)  #true because name are equal of oth car2 and car3
# print(car2.model==car1.model)


   

# print(Cars.model(20000))


#_________________inheritance______________________

#inherit
# class Vechile:    #Base class
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price

#      #funcion call by itself   
#     def load(self,place):       
#          print(f"{self.name} is in {place}")

# class Vechile_1(Vechile):  #parent class
#     def Bike(model):
#         pass

# class Vechile_2(Vechile):   #child class
#     def Scooter(color,company):
#         pass
        
        

# #These all inherit the attributes of base class

# car=Vechile("maruti","2lakh")#call class 1 object

# car1=Vechile_1("Verna","3lakh") #call class -2 objects

# car2=Vechile_2("scorpio",40000)

# print(car.name,car.price)   #class-1

# print(car1.name,car1.price)   #class-2

# print(car2.name,car2.price)   #class-3

# #call class -1 second function

# car.load('Mohali')    
# car1.load('jaipur')
# car2.load('Chandigarh')


# #extend the functionality
# class Vechile:  
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price

#      #funcion call by itself   
#     def load(self,place):       
#          print(f"{self.name} is in {place}")


# class Vechile_1(Vechile):  #parent class
#     def __init__(self,name,price,model):
#         super().__init__(name,price) #call base class
#         self.model=model

#     def work(self):
#         print(f"{self.name} is working")  #call only in this class


# class Vechile_2(Vechile):   #child class
#     def __init__(self,name,price,model,place):
#         super().__init__(name,price) #call base class
#         self.model=model
#         self.place=place


#     def Book(self):
#          print(f"{self.name} is Booked")
        

# Bk=Vechile_1("Kawasaki",2000,2005)    
# k1=Vechile_2("ninja",2000,2005,"chd")

# Bk.work()
# print(Bk.model)    #class 2

# k1.Book()
# print(k1.place)  #class 3


# #___________function overiding---call same function in one another class
# class Vechile:  
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price

#      #funcion call by itself   
#     def load(self,place):       
#          print(f"{self.name} is in {place}")

#     def work(self):
#         print(f"{self.name} is working")      


# class Vechile_1(Vechile):  #parent class
#     def __init__(self,name,price,model):
#         super().__init__(name,price) #call base class
#         self.model=model

#     def work(self):
#         print(f"{self.name} is eating")  #call only in this class


# class Vechile_2(Vechile):   #child class
#     def __init__(self,name,price,model,place):
#         super().__init__(name,price) #call base class
#         self.model=model
#         self.place=placeself.p1=person1


#     def Book(self):
#          print(f"{self.name} is Booked")

#     def work(self):
#         print(f"{self.name} is damaging")      
        
# sk=Vechile("maruti",2000)
# Bk=Vechile_1("Kawasaki",2000,2005)    
# k1=Vechile_2("ninja",2000,2005,"chd")

# sk.work()
# Bk.work()
# k1.work()

#Polymorphism

#method _overiding
# class parent:   #same method inside the idd class
    # name='akshay'

# class child(parent):
    # name='shivani'

# oj=child()  
# oj1=parent()
# print(oj.name)
# print(oj1.name)


#example-2
# class Name:
#     def __init__(self,person1,person2):

#         self.p1=person1
#         self.p2=person2   
    

    # def age(self):
#        print (f"{self.p1} is years old..")


# class Work(Name):

#     def age(self):
#         print(f"{self.p2} is years old..")

# oj1=Name('AAAA','hgjgj')      
# oj2=Work('hjj','hgvj')

# oj1.age()
# oj2.age()
        

#example--3
#polymorphism
#morphic functions

#len function used for string
# print(len("string"))
#                      #Both used same funtion 'len' what doing same work
# #len function used for list
# print(len([1,2,3,4,5]))


# #example-2  #passing values in same function doing different tasks
# def add(x,y,z=0):
#     return x+y+z

# print(add(1,2,3))
# print(add(1,2))

# #example-3
# class India:
#     def Capital(self):
#         print("Delhi is our Capital")


#     def Language(self):
#         print("Hindi is our language")


#     def Currency(self):
#         print("Rupees is the Currency of India")


# class USA:
#     def Capital(self):
#         print("Vashington is capital of USA")


#     def Language(self):
#         print("English is language of USA")


#     def Currency(self):   
#         print("Dollar is the currency of USA")     

# obj_Ind=India()  #make object of class
# obj_USA=USA()

# obj_Ind.Capital() #call objects of class
# obj_Ind.Currency()
# obj_Ind.Language()

# obj_USA.Capital()
# obj_USA.Currency()
# obj_USA.Language()

#another method for calling class
# for country in(obj_Ind,obj_USA):
#     country.Capital()
#     country.Currency()
#     country.Language() 

#######function inside class
# class Bird:
#     def intro(self):
#         print("There are many types of birds")

#     def fly(self):
#         print("Most of birds can fly but some can not")    

#     def color(self):
#         print("There are different colors of Birds")    

# class Crow(Bird):
#     def intro(self):
#         print("The name of Bird is Crow")

#     def fly(self):
#         print("crow can fly")    

#     def color(self):
#         print("Crow is always Black in color")


# class Hen(Bird):
#     def intro(self):
#         print("The name of bird is Hen")

#     def fly(self):
#         print("Hen can't fly")   

#     def color(self):
#         print("White in color")    

# oj_Bird=Bird()
# oj_Crow=Crow()
# oj_Hen=Hen()

# oj_Bird.intro()
# oj_Bird.fly()
# oj_Bird.intro()

# oj_Crow.intro()
# oj_Crow.color()
# oj_Crow.fly()

# oj_Hen.intro()
# oj_Hen.fly()
# oj_Hen.color()


# from traceback import print_tb


class  India:
    def Capital(self):
        print("Delhi is the capital of India")

    def Currency(self):
        print("Rupees is our currency")   

class USA(India):

    def Capital(self):
        print("Vashington is the capital of India")

    def Currency(self):
        print("Dollar is our currency") 

def function(obj):    
    obj.Capital()    #we store the objects of class in function

def second(y):
    y.Currency()
        

oj_India=India()
oj_USA=USA()

function(oj_India)
second(oj_USA)


















