# Simple refresh in Python fuctions.
a=int(input("Enter the value of a:"))#Here a and b are global variable.Can be used anywhere inside the program.
b=int(input("Enter the value of b:"))
#User defined functions. 
def add(a,b):#Here a and b in the function definition is called formal parameters.sum refers to function name. 
     print("Sum",a+b)#Function definition.
add(a,b)#Function calling statement where a and b are called actual parameter,also called as arguments.
def difference():#Function with no parameter  and arguments.
    if(a>b):
        print("Difference",a-b)
    else:
        print("Difference of two numbers is not commutative\na-b should be greater than zero")
difference()
def division(a,b=6):#Function with default argument.
    c=a/b #Here c is local variable.Only used in function division.
    if(a>b)and(a>0)and(b>0):
        print("Division of two numbers",c)
division(a,b)
def modulus(a,b):
    print("Remainder=",a%b)
modulus(a,b)
def var_len_args(*n):#Variable length argument,used to read n number of parameters in the function.
    print("Numbers=",(a*b)*n)#Performs like strings (repeatation).
var_len_args(a,b,5)
#Anonymous function.
product=lambda a,b:a*b #Syntax:function_name=lambda arg 1,arg 2:expression to be performed.
print("The product of two numbers:",product(a,b))
def exponent(a,b):
     print(a,"Exponent of",b,"=",a**b)
exponent(a,b)
#Composition function.
a=eval(input("Enter a expression to be performed:"))
print("Solution=",a)#Used to check the precedence of operator in a given expression
#Global variable
def var():
     global b #To access global variable global keyword is used.
print("Accessed variable=",b)
b+=1
print("Modified variable=",b)
var()
#Recursion.
#The function calls itself again and again is called recursion.
n=int(input("Enter the value of n:"))
def factorial(n):
     if(n==0)or(n==1):
          return 1
     else:
          return n * factorial(n-1)
result=factorial(n) #Store the value of factorial to print it.
print("Factorial of",n,"=",result)
#Illustration of built in function starts here.
num1=float(input("Enter the 1st number(Floating point numbers only allowed):"))
num2=int(input("Enter the 2nd number:"))
num3=int(input("Enter the 3rd number(number<0):"))
str1=str(input("Enter the string 1:"))
def built_in(num1,num2,str1):
     print("a=",abs(num1))#abs(variable_name) returns the absolute value of the given number by user.
     print("b=",abs(num2))
     print("c=",ord(str1))#Returns the ASCII value  for the unicode of the  given character.Inverse of chr().
     print("d=",chr(num2))#Returns the unicode for the ASCII value.
     print("e=",bin(num2))#Returns the binary string with prefix 0.
     print("f=",type(str1))#Returns the type of the object.
     print("g=",id(num1))#Returns the address of the object.
     print("h=",format(num2,'b'))#Returns the binary equivalent.
     print("h1=",format(num2,'o'))#Returns the octal equivalent.
     print("h2=",format(num2,'f'))#Returns the fixed point-notation with six digit precision.
     print("i=",round(num1))#Returns the round off value of floating point numbers.(Type conversion)
     print("j=",round(num2,2))#Returns the round off value with user desired decimal(float) places.
     print("k=",pow(num1,num3))#Computes Exponent(a,b i.e a**b)
built_in(num1,num2,str1)
list_1=[2,4,6,8,10]
def built_in_for_list(list_1):
     print("Maximum element of the list=",max(list_1))
     print("Minimum element of the list=",min(list_1))
     print("Sum of the elements in List_2:",sum(list_1))
built_in_for_list(list_1)
#Math function
import math
print(math.floor(num1))#Returns the largest integer (compared in accordance with real,mantissa part in float numbers)
print(math.floor(num3))
print(math.ceil(num1))
#Inverse of floor().(Returns smallest integer)
print(math.ceil(num3))
print(math.sqrt(num2))#Computes square root of a given number>0.




     

