import math

##Eq1
print("Equation 1 : x ^2 + cos x ^ 2 ")
x1 = float(input("Enter value x (degree angle) : "))
print("x = " , x1)
x1_s = math.radians(x1)
sin_x = math.sin(x1_s)
cos_x = math.cos(x1_s)
r1 = sin_x**2 + cos_x**2
print("Value of sin x ^2 + cos x ^ 2 is ",r1)
print()

##Eq2
print("Equation 2 : e^(0.5 sqrt( tan cos x)) ")
x2 = float(input("Enter value x (degree angle <= 90) : "))
print("x = " , x2)
if x2 > 90:
    print("Error: Please enter value x (degree angle <= 90)")
else:
    x2_s = math.radians(x2)
    cos_x = math.cos(x2_s)
    tan_cos_x = math.tan(cos_x)
    sqrt_tan_cos_x = math.sqrt(tan_cos_x)
    r2 = math.exp(0.5 * sqrt_tan_cos_x)
    print("Value of e^(0.5 sqrt( tan cos x) is ",r2)
print()

##Eq3
print("Equation 3 : [ log(x^2/(1-x)) ] / [ x^(5+x)] ")
x3 = float(input("Enter value x (0.0 - 1.0 ) : "))
print("x = " , x3)
if x3 <= 0 or x3 >= 1:
    print("Error: Please enter value x (0.0 - 1.0 )")
else:
    l1 = math.log(x3**2/(1-x3))
    l2 = x3**(5+x3)
    r3 = l1/l2
    print("Value of [ log(x^2/(1-x)) ] / [ x^(5+x)] is ",r3)
print()


