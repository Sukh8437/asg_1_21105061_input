print("---Assignment04---")



print("question_1")

print("To solve the problem of tower of hanoi with three disks")
def hanoi(n, fro, to, aux):
    if n==0:
        return

    hanoi(n-1, fro, aux, to)
    print(f"Move Disk {n} from {fro} to {to}")
    hanoi(n-1, aux, to, fro)

#calling fuction
hanoi(3, 'A', 'C', 'B')
print("")




print("question02")

n=int(input("enter the number of rows in Pscal's Triangle: "))

#Using Recurssions
print("\nUsing recursions:\n")
def pascal(n, originaln=n):
    if n==0:
        return

    pascal(n-1,originaln)

    #To print spaces
    print(' '*(originaln-n), end='')

    #first number always equals to 1
    entry=1
    for i in range(1, n+1):
        print(entry, end=' ')

        #Using binomail coefficients
        entry=entry*(n - i)//i
    print()
pascal(n)

#Using loops
print("\nUsing loops:\n")
for line in range(1, n+1):

    print(' '*(n - line), end='')

    x=1
    for i in range(1, line+1):
        print(x, end=' ')
        x=x*(line - i)// i
    print()
print("")


        
        

print("question03")

a=int(input("Enter the first interger: "))
b=int(input("Enter the second interger: "))
c=a%b
d=a//b
print("Reminder is: ",c)
print("Quotient is: ",d)
if(c!=0):
    if (d!=0):
        print("Both values are non zero")
    else:
            print("One value is zero")
else:
    if(d!=0):
        print("One value is zero")
    else:
        print("Both values are zero")

set1=set()
for i in range(4,7):
    f=c+i
    g=d+i
    if(f>4):
        set1.add(f)
        print(set1)
    if(g>4):
        set1.add(g)
        print(set1)

print(set1)
set2=frozenset(set1)
print("Immutable set:",frozenset(set1))
print("Largestvalue in set: ",max(set2))
k=max(set2)
print("Hash value: ",hash(k))
print("") 
 



print("question04")

class Student:
    def __init__(self, student, sid):
        self.name = student
        self.sid = sid
    
    def __del__(self):
        print("Object destroyed")

#creating object
student1 = Student("Sukhwinder Kaur", 21105061)
print("Object created")

#printing the assigned values
print(f"The name of the student is {student1.name} and SID is {student1.sid}.")

#deleting object
del student1
print("")




print("question05")


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __del__(self):
        print(f"Employee {self.name} record deleted")

#creating employee records
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

#part a, updating salary
employee1.salary = 70000
print(f"a. The updated salary of the employee {employee1.name} is {employee1.salary}")

#part b, deleting a record
print("b. ", end='')
del employee3
print(" ")



print("question06")

print(" ")
# word from the first friend
word = input("Enter the first word: ")

# a meaningful word with the exact same letters
testword = input("\nEnter a new meaningful word to test your friendship: ")

#defining dictionary from last assignment
def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count

# to verify the letters of the new word
if count_in_dict(word) != count_in_dict(testword):
    print("The letters aren't exact, friendship is fake!!")

#shopkeeper's input to verify the word's meaning
def userinput():
    ans = input("\nDoes the word makes sense?(y or n)\n")

    if ans == 'y':
        print("The friends pass the friendship test!!\n\n")
    elif ans == 'n':
        print("The word doesn't have a meaning, friendship is fake!!\n\n")
    else:
        print("Invalid input, try again")
        userinput()
userinput()
print("")



            
