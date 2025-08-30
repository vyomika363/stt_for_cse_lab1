"This is a function to greet, and then print the greatest and smallest values"
print("Hello world")
print("This is STT for CSE lab 1")

NUM_1= 10
NUM_2= 14
NUM_3= 12

def greatest_num(a,b,c):
    "This is a function for the greatest value."
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c

def smallest_num(a,b,c):
    "This is a function for the smallest value."
    if a <= b and a <= c:
        return a
    if b <= a and b <= c:
        return b
    return c

#Now we have defined 2 functions which will return the greatest and smallest
#They take int inputs and return int outputs

L= greatest_num(NUM_1,NUM_2,NUM_3)
S=smallest_num(NUM_1,NUM_2,NUM_3)

print("greatest number here is ", L)
print("smallest number here is ", S)
