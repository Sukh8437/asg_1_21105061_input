#Assignment -02


#ques1.a
string="Python is a case sensitive language"
length=len(string)
print("The length of string is",length)

#ques1.b
string="Python is a case sensitive language"
R_string=string[::-1]
print("The reversed string is",R_string)

#ques1.c
good="Python is"
good1=good+ ' a case sensitive'
print(good1)

#ques1.d
string="Python is a case sensitive language"
string2=string.replace('a case sensitive','object oriented')
print(string2)

#ques1.e
string="Python is a case sensitive language"
fnd=string.find('a')
print("The index of 'a' is ",fnd)

#ques1.f
string="Python is a case sensitive language"
string3=string.replace(" ",'')
print(string3)


#ques2
name="Sukhwinder Kaur"
SID="21105061"
department="ECE"
CGPA="9.9"
output="Hey,"+name +" Here!\n"+"My sid is "+SID+"\nI am from "+department+" and my CGPA is "+CGPA
print(output)


#ques3.a
a=56
b=10
print("The value of a AND b is ",a&b)

#ques3.b
print("The value of a OR b is ",a|b)

#ques3.c
print("The value of a XOR b is ",a^b)

#ques3.d
print("The value of a after left shift with 2 bits is ",a<<2)
print("The value of b after left shift with 2 bits is ",b<<2)

#ques3.e
print("The value of a after right shift with 2 bits is ",a>>2)
print("The value of b after right shift with 4 bits is ",b>>4)

#ques4
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
num3=int(input("enter third number:"))
if num1>num2 and num1>num3:
 print("The greatest of three number is :",num1)
elif num2>num1 and num2>num3:
 	print("The greatest of three number is :",num2)
else:
	print("The greatest of three number is :",num3)


#ques5
stat=input("write your string here:")
print(stat)
if "name" in stat:
	print("Yes")
else:
	print("No")


#ques6
s=input("side no 1 of triangle :")
k=input("side no 2 of triangle :")
t=input("side no 3 of triangle :")
a=int(s)
b=int(k)
c=int(t)
if a<b+c and b<a+c and c<a+b:
	print("Yes")
else:
	print("No")