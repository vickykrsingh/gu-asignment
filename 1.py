# 1. Explain the concept of Python tuples and illustrate how to access values in tuples, update
# tuple elements, and delete elements from tuples using a program. Clarify the concept of
# anonymous (lambda) functions in Python, outlining their definition and primary use
# cases. Furthermore, present a brief Python code snippet exemplifying the creation and
# application of a lambda function.

# a tuple is an ordered and immutable collection of elements, defined using parentheses.
# Tuples maintain the order of elements, and once created, their elements cannot be modified.
# They are commonly used to represent a fixed set of values that should remain constant during program
# execution, providing a means to ensure data integrity by preventing inadvertent changes.
# program : 
t1=(10,20,30,40,50);
print(t1[0]) #accessing tuple element output : 10
# directly updation of tuple element are not allowed so we convert into list and then update the list and agin convert into tuple.
t2=list(t1) #converting into list
t2.pop(); #deleting list element
t2[2]=100; #assigning new value at the third index into list
print(t2[2]) #accessing 2nd index of t2 list
t1=tuple(t2) #again converting into tuple
print(t1) #(10, 20, 100, 40)

# lambda function is short syntax of standard function and it is also used for passing argument as a value to the other function.
#syntax of lambda function:
sum = lambda a,b : a+b;
print(sum(20,30)) #output : 50