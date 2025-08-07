#area calculator
import math
import decimal
decimal.getcontext().prec = 50
def Main():
    #banner
    print('=====================')
    print('   Area Calculator   ')
    print('=====================')
    #Main Menu / Asking for what shape
    global gb
    print('1) Triangle')
    print('2) Rectangle')
    print('3) Square')
    print('4) Circle')
    print('5) Quit')
    shape = int(input('What is the Shape of the object ? '))
    print('')
    if shape == 1:
        gb = Tri
        Tri()
    elif shape == 2:
        gb = Rec
        Rec()
    elif shape == 3:
        gb = Sqa
        Sqa()
    elif shape == 4:
        gb = Cir
        Cir()
    elif shape == 5:
        quit
    else:
        print('Invalid Answer')
        Main()
#If Shape is a Triangle
def Tri():
#    goback == 0
    print('***Triangle Area Calculator***')
    base = decimal.Decimal(input('Base? '))
    height = decimal.Decimal(input('Height? '))
    print('')
    print('The area is: ',round(((base*height)/2),3))
    GoBack()
#If Shape is a Rectangle
def Rec():
    print('***Rectanlge Area Calculator***')
    length = decimal.Decimal(input('Length? '))
    width = decimal.Decimal(input('Width? '))
    print('')
    print('The area is: ',round(decimal.Decimal((length*width)),3))
    GoBack()
#If Shape is a Square
def Sqa():
    print('***Square Area Calculator***')
    s1 = decimal.Decimal(input('Length of one side? '))
    print('')
    print('The area is: ',round((s1 ** 2),3))
    GoBack()
#If Shape is a Circle
def Cir():
    print('***Circle Area Calculator***')
    rad1 = decimal.Decimal(input('Radius? '))
    print('')
    print('The area is: ',round(decimal.Decimal(math.pi) * (rad1 ** 2),3))
    GoBack()
def GoBack():
    goback = 0
    while goback != 1 and goback != 2:
        print('')
        print('1) Again?')
        print('2) Main Menu')
        goback = int(input())
        if goback == 1:
            gb()
        elif goback == 2:
            Main()
        else:
            print('Invalid Input')
Main()