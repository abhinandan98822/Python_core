# for i in range(1,7):
#     print("*"*i)   #left triangle

# a=8
# for i in range(1,7):   #print complete triangle
#     print(" "*(a-i)+" *"*i)

# a=8
# for i in range(1,7):
#     print(" "*(a-i)+"*"*i) 

# a=9
# for i in range (1,a):
#     print(" * "*i+" "*(a-i)+"*"*i)

#square
# a=9
# for i in range(a):
#     for j in range(a):
#         print(i,end=" ")
#     print(" ")    


#square
# a=8
# for i in range(1,8):
#     print("* "*a)

#opposite triangle
# a=7
# for i in range(1,7):
#     print("*"*(a-i))   #opposite left triangle

# a=9
# for i in range(9,0,-1):
#     print(" "*(a-i)+"* "*i)   #print opposite triangle

# a=8
# for i in range(a,0,-1):
#     print("  "*(a-i)+"* "*i)  #riight opposite triangle


#while loop
# a=1
# while  (a<11):
#     print("*"*a)   #LEFT TRIANGLE
#     a+=1 

# a=1
# while(a<12):
#     print(" * "*11)
#     a+=1


#triangle with while loop
# a=1
# while(a<12):
#     print(" "*(11-a)+"* "*a)    #complete triangle
#     a+=1

#recursion
# def function(c):
#     c+=1
#     if (c == 10):
#         return
#     print(c)
#     function(c)


# function(0)

#lamvda
n=lambda a,v:a+v
print(n(1,2))

    