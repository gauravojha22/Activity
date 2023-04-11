#Arithmetic
a = float(input())
b = float(input())
sum = a + b
print("sum of numbers is:",sum)
diff = a - b
print("The difference of  numbers is:",diff)
mult = a*b
print("Multiplication of  numbers is:",mult)
div = a/b
print("Division of numbers is:",div)
mod = a%b
print("Remainder of  numbers is:",mod)
fd = a//b
print("Floor division of two entered number is:",fd)

#Conversion
#Micrometer to meter
um = float(input()) 
m = um*pow(10,-6)
print(m)

#Astronomical unit to meter
AU = float(input())
mt = AU*1.496*pow(10,11)
print(mt)

#Earthquake Impact
a = float(input())
if 1.0<=a<2:
    print("Micro")
elif 2<=a<4:
    print("Minor")
elif 4<=a<5:
    print("Light")
elif 5<=a<6:
    print("Moderate")
elif 6<=a<7:
    print("Strong")
elif 7<=a<8:
    print("Major")
elif 8<=a<10:
    print("Great")

#Factor
T = float(input("Enter temperature in degree Celsius:"))
V = float(input("Enter wind speed in Kmph:"))
WC = 13.12 + 0.6215 * T * ((0.3965 * T) - 11.37) * V**0.16
print(WC)
