N = int(input('Enter the wavelength in nm: '))
if N>=380 and N<450:
    print('Violet')
elif N>=450 and N<495:
    print('Blue')
elif N>=495 and N<570:
    print('Green')
elif N>= 570 and N<590:
    print('Yellow')
elif N>=590 and N<620:
    print('Orange')
elif N>=620 and N<750:
    print('Red')
else:
    print('Inappropriate wavelength')
