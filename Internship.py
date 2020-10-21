print("practice 01")
import datetime

x = datetime.datetime.now()
print(x)

#02
print("practice 02")
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

#03
print("practice 03")
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

#04
print("practice 04")
import platform

x = dir(platform)
print(x)

#05
print("practice 05")
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#06
print("practice 06")
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#07
print("practice 07")
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#08
print("practice 08")
print(10 > 9)
print(10 == 9)
print(10 < 9)

#09
print("practice 09")
x = 200.6
print(isinstance(x, float))

#10
print("practice 10")
def myFunction() :
  return False

if myFunction():
  print("YES!")
else:
  print("NO!")


#11
print("practice 11")
x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list

#12
print("practice 12")
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#13
print("practice 13")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Negative indexing means starting from the end of the list.

#This example returns the items from index -4 (included) to index -1 (excluded)

#Remember that the last item has the index -1,

#14
print("practice 14")
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#15
print("practice 15")
thislist = ["apple", "banana", "cherry"]

thislist.append("orange")

print(thislist)


#16
print("practice 16")
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


#17
print("practice 17")
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#18
print("practice 18")
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#19
print("practice 19")
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("hamza", 23)

print(p1.name)
print(p1.age)

#20
print("practice 20")
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("hamza", 23)
p1.myfunc()


#21
print("practice 21")
#The try block does not raise any errors, so the else block is executed:

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

#22
print("practice 22")
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

#23
print("practice 23")
name=input("enter your name: ")
age=input("enter your age: ")
print("your name is " +name ,"and age is", age)




#24
print("practice 24")
print("-----------------\n Number Checking \n-----------------\n")
a=input("enter a: ")
b=input("enter b: ")

if a > b:
  print("a is greater than b")
elif a == b:
  print("a and b are equal")
else:
    print("b is greater")



#25
print("practice 25")
