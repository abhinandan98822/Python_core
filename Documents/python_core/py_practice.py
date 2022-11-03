#? print Hello
print("hello")

#?comments in python
"""
This is comments in python
"""
print('comments are shown above')

#?assign value to single variable
a=12
print(a)

#?assign value to the multiple variables
x,y,z="Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#?different variables have same 
x=y=z="orange"
print(x)
print(y)
print(z)

#?unpack collection
fruits=["orange","apple","grapes"]
a=b=c=fruits
print(a)
print(b)
print(c)

x = "Python is awesome"
print(x)

#?know the type of variable
x = 5
print(type(x)) 

y=4.6
print(type(y))

z="name"
print(type(z))

p=2/3
print(type(p))

a=2
b=2
c=a is b
print(type(c))

#? slicing strings
b="hello world"
print(b[:5])
print(b[1:5])

#? modify string
#!uppercase
a="Hello world"
print(a.upper())

#!lowercase
b="hello world"
print(b.lower())

#!remove whitespace
c=" Hello , world "
print(c.strip())             #!removing the white space
print(c)

#!replace method
a="Hello,world"
print(a.split(","))

#?concatenate string
a="hello"
b="world"
c=a+" "+b
print(c)

#?format string
a=23
b="hello my name is abhinandan and i am {}"
print(b.format(a))

a="hello my name is {}{}{}{}"
b="abhinandan "
c="and i am "
d= 23
e=" years old"
print(a.format(b,c,d,e))

#?escape characters
text="hello my name is \"abhinandan\" and i am 23 years old"
print(text)

#************************ python operators********************
#!Airthmatic operators
a=2
b=4
print(a+b)  #?addition
print(b-a)  #?substraction
print(a*b)  #?multilication
print(b/a)  #?divide
print(b//a) #?floor division
print(a%b)  #?modulus
print(a**b)  #?exponantiation


#!Comparison operator
a=6
b=5
print(a==b)
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)
print()

#!Assignment operator
a=6
a +=3
b=4
b -=2
c=5
c *=2
d=10
d //=2
e=12
e >> 2
print(a)
print(b)
print(c)
print(d)
print(e)

#!Logical operator
x=5  
print(x>3 and x<7)
print(x>3 or x<7)

#! identity operator
a=6
b=7
print( a is b)
print( a is not b)

#! membership operator
a=[1,2,3,4,5]
b=4
print(b in a)
print(b not in a)

#! bitwise operator
a=5
b=7
print(a & b)
print(a | b)
print(~ a)
print( ~ b)
