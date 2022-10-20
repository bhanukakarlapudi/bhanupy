# for i in range(1,500,):
#     if i**2<=500:
#      print(i**2)         #perfect squares
# a=["chinnu","9.7","21"]
# for i in a:
#     print(i)
    
# for i in range(1,101):
#     if i%2==0 or i%5==0:
#         continue;
#     print(i)
# print("bye")


# av=12
# a=int(input("how many drinks u want?" ))
# i=1
# while i<=a:
#     if i>av:
#         print("out of stock")
#         break;
                               
#     print("drink")
#     i+=1

##for even/odd numbers

# for i in range(1,101):
#     if i%2==0:
#         pass
#     else:
#         print(i)
# print("bye")

 #fabonacci series
# a=0
# b=1
# print(a)
# print(b)
# for i in range(10):
  
#     c=a+b
#     print(c)
#     a=b
#     b=c
   

# for i in range(1,10):
#    for j in range(0+i):
#      print("@",end="")

#    print()     

# a=99
# for i in range(2,a):
#   if a%i==0:
#     print("not a prime")
#     break;
# else:
  # print("prime")  //prime number//

# from array import *
# vals=array('L',[12,21,11,33,44])
# vals.reverse()
# print(vals)            //array in python//
# for i in vals:
  # print(i)

# for row in range(6):
#   for col in range(7):
#    if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
#     print("*",end="")
#   else:
#    print(end="")
#   print()

# from array import *
# from curses import def_prog_mode
# from email.errors import MisplacedEnvelopeHeaderDefect
# from locale import RADIXCHAR
# from typing_extensions import Self
# arr=array('i',[])

# n=int(input("enter the length of array"))

# for i in range(n):
#   x=int(input("enter the value"))
#   arr.append(x)

# print(arr)


# k=0
# val=int(input("enter the value for search"))
# for e in arr:
#   if e==val:
#     print(k)
#     break
#   k+=1


#ways of creating array using numpy

# from numpy import*

# arr=array([1,2,3,4,5,6,67])
# print(arr)

# from numpy import *

# arr = linspace(1,50,3,)

# arr=arange(0,20,2)

# arr=logspace(1,20,5)

# arr=zeros(10)

# arr=ones(7,int)

# print(arr)

# from numpy import *
#
# arr1=array([3,4,5,6,7,8,9])
# arr2=array([5,6,7,4,3,6,7,3])

# print(concatenate([arr1,arr2]))

# print(sqrt(arr1))


# for i in arr1:
  #  arr1+=5
  #  print(arr1)
  #  break

# from numpy import *
# arr1=array([1,2,3,4,5])
# arr2=array([4,5,6,7,8])
# for i in range (len(arr2)):
#   arr3=arr1[i]+arr2[i]
#   print(arr3)

# arr=array([1,2,3,4,5])
# for i in arr:
#   if i==max(arr):
#    print(i)



# from turtle import *
# speed(50)
# color('cyan')
# bgcolor('black')
# b=200
# while b>0:
#   left(b)
#   forward(b*2)
#   b=b-1

# matrices
# from numpy import *
# arr1=array(
#             [[1,2,3],
#            [3,2,1]]
#            )
# arr2=array(
#             [[4,5,6],
#             [6,5,4]]
            # )
# m=matrix('1 2 3;4 5 6;7 8 9')

# print(m.diagonal)

# FUNCTIONS IN PYTHON - BLOCK OF CODE USED FOR RECALL 

# def bhanu():
  # print("bsc student")
  # print("final year")
# bhanu()

# def add(a,b):
#   c=a+b
#   print(c)

# result=add(43,34)

# def add_sub(a,b):
#   x=a+b
#   y=a-b
#   return x,y
# result1 ,result2 = add_sub(12,12)
# print(result1,result2)

# def name():
  # print('prince')
# name()

# def update(x):
  # x= 4
  # print("x",x)

  # a=10
  # update(a)
  # print("a",a)
#types of arguments - formal,actual(position,keyword,defualt,var len)

# def std(nam,age):
#   print(nam)
#   print(age+2)

# std("prince",31)

 # def add(a,*b)      position of argmts
#   c=a
#   for i in b:
#     c=c+i
#   print(c)
# add(21,32,3)

# def emp(name,**data):             //kwargmts//
#   print(name)
#   for i ,j in data.items():
#     print(i,j)
# emp("mr.B",age=22,city="hyd",ph=434133)

# a=23
# print(id)
# def none():
#   a=31                     //global keyword//
# y=globals()['a']
# print(y)
# none()

# print(a)

# //passing list to a function
# def count(list):
#   even=0
#   odd=0
#   for i in list:
#     if i%2==0:
#       even+=1
#     else:
#       odd+=1


#     return even, odd

# list =[2,12,23,75,98,64,32]

# even, odd = count(list)
  
# print(even)
# print(odd)

# def fib(n):

#   a = 0
#   b = 1
   
#   if n == 1:
#      print(a)
#   else:
#     print(a)
#     print(b)

#     for i in range(2,n):
#         c=a + b 
#         a = b
#         b = c
#     print(c)


# fib()

# def fact(n):
#   f=1
#   for i in range(1,n+1):
#     f=f*i

#   return f

# x=4

# result=fact(x)

# print(result)

# import sys

# sys.setrecursionlimit(1500)
# print(sys.getrecursionlimit())

# i=0
# def good():
#   global i
#   i=i+1                 //recursion:function calls itself //
#   print("mrng!",i)
#   good()

# good()

# sub=lambda a:a-4      // lambda anonymous funnction
# print(sub(10))

# from functools import reduce


# num=[1,2,5,6,8,3,7,3]

# evens=list(filter(lambda n:n%2==0,num))
# print(evens)

# odds=list(filter(lambda n:n%2!=0,num))
# print(odds)

# add=reduce(lambda a,b:a+b,odds)
# print(add)

# doubles=list(map(lambda n:n*2,evens))
# print(doubles)

# sum=reduce(lambda a,b:a+b,evens)
# print(sum)
# print(__name__)


# class name:        //opps: obj,clss,abstraction,inheritance,encapsulation,polynerism

#  def intial():
#    print("kakarlapudi,bhanu")

# nme1=name()
# nme2=name()

# name.intial()


# class bike:
#   wheels=2

#   def _init_(self):
#      self.mil = 45
#      self.com = "rx"


# # c1 = bike()
# c2 = bike()

# print(c1.com , c1.mil , c1.wheels)
# print(c2.wheels)

# import sys

# print(sys.path)

# import time
 

# print(time.localtime(time.time()))
# print(time.asctime(time.localtime(time.time())))

# import datetime

# print(datetime.datetime.now())
# print(datetime.datetime(2022,11,9,12,11,21))


# import calender
# yy=2022
# mm=11
# print(calender.month(yy,mm))  

# class emp:
#   rollno=21
#   name="bhanu"
#   def display(self):
#     print(self.rollno,self.name)


from turtle import *
bgcolor('yellow')
right(90)

pos =[(-40,0),(40,0)]
for x,y in pos:
  up()
  goto(x,y)
  down

fillcolor('red')
begin_fill() 
for i in range(2):
 forward(200)
 left(90)
 forward(40)
 left(90)
 end_fill()
up()
goto(-40,0)
down()
left(22)
begin_fill()
for i in range(2):
 forward(217)
 left(68)
 forward(40)
 left(112)
end_fill()