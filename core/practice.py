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


#call classes y inherit the objects of first class
class Country:
    def __init__(self,name,currency,population):
        self.name=name
        self.currency=currency
        self.population=population

    def Capital(self): 
        print(f"{self.name} is our country and {self.currency} is our Currency and {self.population} is our population") 

class State(Country):
    super.__init__(self,name,)

     def Cap(self):
         print(f"{self.name} is our state and {self.currency} is our currency and {self.population} is population")

oj1=Country('India','Rupees','125 billion')
oj1.Capital() 

oj2=state()








