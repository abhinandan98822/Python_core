#ENCAPSULATION-Hiding data implementation,and the their is only one method ouside to access data

# class Data:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         #can be access by print name
#         self._salary=None        #single underscore "_" is called protected attribute."not fully  private"
#        ### self.__address="MOhali"    #double underscore "__" is called completely private attribute
#         self._num_bug_solved=0

#     #getter 
#     def get_salary(self):
#         return self._salary

#     #setter
#     def set_salary(self,value):  
#         self._salary=value

# obj=Data("Akshay",25)
# print(obj.age,obj.name,)

# obj.set_salary(15000)   #pass the value to the method set_salary
# print(obj.get_salary())  #print salary













