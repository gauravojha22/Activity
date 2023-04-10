def Hotel (Type_room,days,food_price):
    if Type_room == 'Delux room':
        a = 7500*days
        print('price_of_stay:',a)
        sgst = 0.09*food_price
        cgst = 0.09*food_price
        tip = 0.1*food_price
        print('SGST:', round(sgst, 2)) 
        print('CGST:', round(cgst, 2)) 
        print('Tip:', round(tip, 2))
        print('Grand total for meal:', c+sgst+cgst+tip)
        
    elif Type_room =='Non AC Room':
        a = 4500 * days
        print('price_of_stay:', a)
        sgst = 0.025 * food_price
        cgst = 0.025 * food_price
        tip = 0.1 * food_price
        print('SGST:', round(sgst, 2))
        print('CGST:', round(cgst, 2)) 
        print('Tip:', round(tip, 2))
        print('Grand total for meal:', c+sgst+cgst+tip)
    else:
        print('Invalid room Type')
a = input('Type of room: ') #Type_room
b = int(input('Number of days you stayed: ')) #days
c = int(input('Total food amount: ')) #food_price

Hotel(a,b,c)
