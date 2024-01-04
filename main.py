# This is a sample Python script.

# Press Ctrl+R to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Meta+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    # """
    # A simple hello world script
    # """
    #
    # def print_hi(name: object) -> object:
    #     # Use a breakpoint in the code line below to debug your script.
    #     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    #
    #
    # """
    # A simple function that takes a text variable, and use it in string formating which is printed
    # """
    #
    # # Press the green button in the gutter to run the script.
    # # if __name__ == '__main__':
    #
    # string = "PyCharm"
    # print_hi(string)

    print("Hello, World!")

    if 5 > 2:
        print("Five is greater than two!")

    x = 5
    y = "Hello, World!"

    x = 5
    L = "John"
    print(x)
    print(y)
    print(L)
    x = str(3)  # x will be '3'
    y = int(3)  # y will be 3
    z = float(3)  # z will be 3.0
    print(type(x))
    print(type(y))
    fruits = ["apple", "banana", "cherry"]
    x, y, z = fruits
    print(x)
    print(y)
    print(z)
    print(x), print(y)
    x = "Python "
    y = "is "
    z = "awesome"
    print(x + y + z)
    x = 5
    y = "John"
    print(x, y)

    x = "awesome"


    def myfunc():
        x = "fantastic"
        print("Python is " + x)


    myfunc()

    print("Python is " + x)


    def myfunc():
        global x
        x = "fantastic"


    myfunc()

    print("Python is " + x)

    x = "awesome"


    def myfunc():
        global x
        x = "fantastic"


    myfunc()

    print("Python is " + x)
    x = 8
    complex(x)
    print(x)

    x = 35e3
    y = 12E4
    z = -87.7e100
    print(x, y, z)

    x = 3 + 5j
    y = 5j
    z = -5j
    print(x, y, z)

    import random

    print(random.randrange(1, 10))

    for x in "banana":
        print(x)

        a = "Hello, World!"
        print(len(a))

    b = "Hello, World!"
    print(b[2:5])

    b = "Hello, World!"
    print(b[:5])

    b = "Hello, World!"
    print(b[2:])

    b = "Hello, World!"
    print(b[-5:-2])

    a = "Hello, World!"
    print(a.upper())

    a = "Hello, World!"
    print(a.lower())

    a = "      Hello,     World! "
    print(a.strip())  # returns "Hello, World!"

    a = "Hello, World! H"
    print(a.replace("H", "J"))

    a = "Hello, World!"
    print(a.split(","))  # returns ['Hello', ' World!']

    txt = "We are the so-called \"Vikings\" from the north."
    print(txt)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# difference between lists for loops and comprehensions
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
        print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


newlist = [x for x in fruits if x != "apple"]

newlist = [x for x in fruits]

newlist = [x for x in range(10)]

newlist = [x.upper() for x in fruits]

newlist = ['hello' for x in fruits]

newlist = [x if x != "banana" else "orange" for x in fruits]


# Sort lists:
#Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#Sort the list alphabetically: / Sort the list numerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort the list descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


#Reverse the order of the list items:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# 2 ways to copy the lists:
# new list = <previous list>.copy()
#new list=list(<previous list>)
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# List Methods
#
# Python has a set of built-in methods that you can use on lists.
# Method 	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# all about tuples
linda_tuple = ("bio", "programming", "study", "love", "pry", "good")
print (linda_tuple)
print (type(linda_tuple))


#try something!!
thistuple = tuple(["apple", "banana", "cherry"]) # note the double round-brackets
print(thistuple)

print (linda_tuple[1],linda_tuple[-1],linda_tuple[0:2],linda_tuple[:2],linda_tuple[3:])
if "bio" in linda_tuple:
    print ("yes 'bio' in the tuple")
#print ('yes,'bio' in the tuple')
#print ('yes,'bio' in the tuple')
          # ^^^^^^^^^
#SyntaxError: invalid syntax. Perhaps you forgot a comma?
lindalist = list(linda_tuple)
lindalist.remove("bio")
lindalist[1] = "linda"
lindalist.append ("career")
linda_tuple= tuple(lindalist)
print(linda_tuple)

#2 ways to add tuples :
linda_tuple += thistuple
print(linda_tuple)

sumtuple = linda_tuple + thistuple
print(sumtuple)

(home, *land, earth) = linda_tuple

print(home, land, earth)

for i in range(len(linda_tuple)):
  print(linda_tuple[i])

for x in linda_tuple:
  print(x)

  i = 0
  while i < len(linda_tuple):
      print(linda_tuple[i])
      i = i + 1

linda_tuple = linda_tuple * 2
print(linda_tuple)

L = linda_tuple.count("linda")
A = linda_tuple.index("programming")
print(L , A)


