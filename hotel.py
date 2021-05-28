print ("Welcome to Continental Hotel")
print(" ")
bill = 0
class hotel:

    def Menu(s):
        global bill
        print("Press 1 for Veg \nPress 2 for Non-Veg")
        print("")
        num = int(input("Enter your choice: "))
        if (num == 1):
            print("You have chose Veg Menu")
            y=Veg()
            y.Menu()
            x.Menu1()
        if (num == 2):
            print("You have choose Non-Veg Menu")
            z=NonVeg()
            z.Menu1()
            x.Menu1()

    def Menu1(s):
        global bill
        print(" ")
        print("Press 1 for Re-Order \nPress 2 for Total Bill \nPress 0 for exit")
        print(" ")
        num = int(input("Enter your choice: "))
        if (num == 0):
            pass
        if (num == 1):
            x.Menu()
        if (num == 2):
            print("Your Total bill: ",bill)

class Veg(hotel):
    
    def __init__(s):
        s.Pasta = 40
        s.Biryani = 400
        s.Nachos = 180
        s.Pizza = 400

    def Menu(s):
        global bill
        dict = {1:"1 Pasta = Rs 40",
                2:"2 Biryani = Rs400 ",
                3:"3 Nachos= Rs 180",
                4:"4 Pizza= Rs400"}
        print(dict[1])
        print(dict[2])
        print(dict[3])
        print(dict[4])

        
        a=int(input("Enter your choice: "))
        if (a == 1):
            print("Pasta")
            num=int(input("Please enter Quantity: "))
            if (num > 1 ):
                num = num * s.Pasta
                bill = bill + num
                print("Price for your Quantity is:", num)
                
        if (a == 2):
            print("Biryani")
            num=int(input("Enter Quantity: "))
            if (num > 1 ):
                num = num * s.Biryani
                bill = bill + num
                print("Price for your Quantity is:",num)
                
        if (a == 3):
            print("Nachos")
            num=int(input("Enter Quantity: "))
            if (num > 1 ):
                num = num * s.Nachos
                bill = bill + num
                print("Price for your Quantity is:",num)
                
        if (a == 4):
            print("Pizza")
            num=int(input("Enter Quantity: "))
            if (num > 1 ):
                num = num * s.Pizza
                bill = bill + num
                print("Price for your Quantity is:",num)

class NonVeg(hotel):
    
    def __init__(s):
        s.Chicken_Tandoor = 300
        s.Biryani = 400
        s.Prawns = 180
        s.Fish = 400

    def Menu1(s):
        global bill
        dict = {1:"1 Chicken Tandoor = Rs 300",
                2:"2 Biryani = Rs400 ",
                3:"3 Prawns= Rs 180",
                4:"4 Fish= Rs400"}
        print(dict[1])
        print(dict[2])
        print(dict[3])
        print(dict[4])

        
        a=int(input("Enter your choice: "))
        if (a == 1):
            print("Chicken Tandoor")
            num=int(input("Please enter Quantity: "))
            if (num > 1 ):
                num = num * s.Chicken_Tandoor
                bill = bill + num
                print("Price for your Quantity is:", num)
                
                
        if (a == 2):
            print("Biryani")
            num=int(input("Enter Quantity: "))
            if (num > 1 ):
                num = num * s.Biryani
                bill = bill + num
                print("Price for your Quantity is:",num)
                
        if (a == 3):
            print("Prawns")
            num=int(input("Enter Quantity: "))
            if (num > 1 ):
                num = num * s.Prawns
                bill = bill + num
                print("Price for your Quantity is:",num)
                
        if (a == 4):
            print("Fish")
            num=int(input("Enter Quantity: "))
            if (num > 1 ):
                num = num * s.Fish
                bill = bill + num
                print("Price for your Quantity is:",num)

x = hotel()
x.Menu()
x.Menu1()
