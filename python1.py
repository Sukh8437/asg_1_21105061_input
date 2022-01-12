# first program
a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
avg=(a+b+c)/3

print("avg is:",avg)


#second program
tax_rate=0.2
stand_ded=10000
dep_ded=3000
grs_inc=float(input("enter the gross income: "))
no_of_dep=int(input("enter no of dependents: "))
tax_inc=grs_inc - stand_ded - (dep_ded*no_of_dep)
tax=tax_inc*tax_rate

print("income tax:",tax)


#third program 
print("student=[SID,Name,Gender,Couse Name ,CGPA]")
student=[21105061,'Sukhwinder','F','ECE',9.8]
print("student=",student)


#fourth program
print("Marks of five students")
marks=[80,54,18,45,56]
print("list before sorting:",marks)
marks.sort()
print("list after sorting:",marks)


#fifth program 
#part A
color=['Red','Green','white','Black','pink','yellow']
color.pop(3)
print(color)

#part B
color[3:4]=['purple']
print(color)