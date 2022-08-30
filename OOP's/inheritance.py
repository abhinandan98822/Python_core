#inherit,extend ,override  #methods
# from defer import return_value


# class GrandParents:   #parent class/Base class 
    # def __init__(self,name,age):
        # self.name=name   #function-1
        # self.age=age
        

    # def work(self):     #function-2
        # print(f"{self.name} is working..")



# class parents(GrandParents):   #we only pass one argument here because others are already passes in grandparent class
    #extend function of grandparent--to parents

    # def __init__(self, name, age,gender):   #function-3
        # super().__init__(name, age)   #this used to call base function
        # self.gender=gender

    # def doin(self):    #Function-4
        # print(f"{self.name} is planting")   



# class Children(GrandParents):

    # def doin(self):       #function-5
        
        # print(f"{self.name} is studying..")
        # print(f"{self.name} is painting..")



# GF=GrandParents("late. Kundan lal kaura",91)  #instance-1
# GM=GrandParents("Vimla kaura",84)

# print(f"The name of Grandfather is {GF.name} and age is {GF.age}")  #function-1
# print(f"The name of Grandmother is {GM.name} and age is {GM.age}") 


# print(GF.work())     #function-2


# prntM=parents("Vinod kaura",63,"male")   #instance-2
# prntF=parents("sunita",52,"female")              #parent call the properties/attriutes of Grandparents

# print(prntM.gender)   #call class parent oe argument y function-3
# print(prntF.gender)

# prntM.doin()   #over-ride-means repeat same function into different classes
# prntF.doin()    #function-4 of parent class

# print(f"{prntM.name} is my father and he is {prntM.age} years old")   #function-1
# print(f"{prntF.name} is my mother and she is {prntF.age} years old")

# print(prntM.work())   #function-2

# CHD1=Children("Abhinandan",23)
# CHD2=Children("Shivakshi",26)  #class #

# CHD1.doin()    # Function-5
# CHD2.doin()



 

