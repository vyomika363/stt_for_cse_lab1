print("Hello world")
print("This is STT for CSE lab 1")

num1 = 10
num2 = 14
num3 = 12

def greatest_num(a,b,c):
  if a >= b and a >= c:
    return a
  elif b >= a and b >= c:
    return b
  else:
    return c

def smallest_num(a,b,c):
  if a <= b and a <= c:
    return a
  elif b <= a and b <= c:
    return c
  else:
    return c

#Now we have defined 2 functions which will return the greatest and smallest values amongst 3 numbers
#They take int inputs and return int outputs

largest= greatest(num1,num2,num3)
smallest=smallest_num(num1,num2,num3)

print("greatest number here is ", largest)
print("smallest number here is ", smallest)
