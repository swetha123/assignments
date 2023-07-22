"""
Q.1. Create two int type variables, apply addition, subtraction, division and multiplications
and store the results in variables. Then print the data in the following format by calling the
variables:
"""
var1 = 100
var2 = 25
add = var1 + var2
sub = var1 - var2
multi = var1 * var2
div = var1 / var2

print("the first variable is ",var1 ,   "and the second variable is ", var2)
print("addition:  ",var1 ,   " + ", var2," = ",add)
print("subtraction:  ",var1 ,   " - ", var2," = ",sub)
print("multiplication:  ",var1 ,   " * ", var2," = ",multi)
print("division:  ",var1 ,   " / ", var2," = ",div)

"""
Q.2. What is the difference between the following operators:
(i) ‘/’ & ‘//’
(ii) ‘**’ & ‘^’
ANS -- (i) / - regular division symbol is used in division to return a floating number. 
          // - floor division used in division to get the integer value as a result.
"""

"""
Q.3. List the logical operators.
ANS -- and , or , not
"""

"""
Q.4. Explain right shift operator and left shift operator with examples.
 ANS -- these are bitwise operations performed to move an integer either to the right or left 
        based on the given number bitwise
"""
# example for right shift
a = 5   # 0000  0101
b = a >> 1
print(b)   # 0000 0010

# example for right shift
c = 5   # 0000  0101
d = c << 1
print(d)   # 0000 1010

"""
Q.5. Create a list containing int type data of length 15. Then write a code to check if 10 is
present in the list or not.
"""

l1 = [1,23,34,45,34,23,34,10,34,34,45,78,98,77,99]
print(len(l1))
k = 0
for i in l1:
    if i == 10:
        print("the given element 10 is present")
        k = 1
        break

if k ==0:
    print("the given list does not contain 10")