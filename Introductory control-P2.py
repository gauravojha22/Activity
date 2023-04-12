Nint=45
Div=1  
sum = 0
while Div<Nint:
   if Nint % Div==0:
        sum = sum+Div
   Div=Div+1 
print(sum)
if sum>Nint:
    print('The number is abundant')
elif sum==Nint:
    print('Sum of divisors and number is equal')
else:
    print('The number is deficient')
