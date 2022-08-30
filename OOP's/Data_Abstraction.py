#_____________________Data-Abstraction_______________________
# DataAbstraction-MEANS HIDE THE DATA OF PARENT CLASS AND CALL IT FROM CHILD CLASS.for eg.-a father starts a business and with he hands over his business
# to his child. after hand over the business is the any prolems comes to the business the son will solved that problem not father

# class shape:   #parent class
#     def area(self):
#         pass    

#     def parameter(self):
#         pass

# class Square(shape):  #class square inherit the properties of shape class
#      def __init__(self,side): #__init__ constructor:call y itself
#         self.side=side


#_______________________________________________________________________


 #the work of the abstraction is to stop user from making object of inherited class (shape)

#ABC-abstract-base-class
from abc import ABC,abstractmethod 

class shape(ABC):      #use ABC under class to stop base class from calling

    @abstractmethod  #decorator
    def area(self):
        pass    

    @abstractmethod
    def parameter(self):
        pass

class Square(shape):  
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side*self.side

    def parameter(self):
        return 4*self.side



##s1=shape() it is not accessed by the user because the shape class is abstracted
sq=Square(5) 
print(sq.area())
print(sq.parameter())


