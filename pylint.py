print("Hello world")
print("This is STT for CSE lab 1")

NUM_1= 10
NUM_2= 14
NUM_3= 12

def greatest_num(a,b,c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    else:
        return c

def smallest_num(a,b,c):
    if a <= b and a <= c:
        return a
    if b <= a and b <= c:
        return c
    else:
        return c

#Now we have defined 2 functions which will return the greatest and smallest    
#They take int inputs and return int outputs

largest= greatest_num(NUM_1,NUM_2,NUM_3)
smallest=smallest_num(NUM_1,NUM_2,NUM_3)

print("greatest number here is ", largest)
print("smallest number here is ", smallest)
