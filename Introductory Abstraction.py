def earth(a,b):
    c = a + b
    print("The sum of two numbers is:",c)
    q = a-b
    print("The subtraction of two number is:",q)
    e = a**b
    print("Exponention of entered two number is:",e)

print(earth(a=float(input()),b=float(input())))

def sc(n):
    inches = n / 2.54
    feet = inches / 12
    yards = feet / 3
    return (inches, feet, yards)
print(sc(n=int(input())))

def earthquake(n):
    if 1.0 <= n < 2:
        return "Micro"
    elif 2 <= n < 4:
        return "Minor"
    elif 4 <= n < 5:
        return "Light"
    elif 5 <= n < 6:
        return "Modernte"
    elif 6 <= n < 7:
        return "Strong"
    elif 7 <= n < 8:
        return "Major"
    elif 8 <= n < 10:
        return "Great"

n = float(input())
print(earthquake(n))


def wc(T,V):
    WC = 13.12 + 0.6215 * T * ((0.3965 * T) - 11.37) * (V**(0.16))
    return WC
T = float(input("Enter temperature in degree Celsius:"))
V = float(input("Enter wind speed in Kmph:"))
print(wc(T,V))
