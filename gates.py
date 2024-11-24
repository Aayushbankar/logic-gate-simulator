# banner designing 
banner = '''
 _                    _            _____         _                       _                    _         _                
| |                  (_)          |  __ \       | |                     (_)                  | |       | |               
| |      ___    __ _  _   ___     | |  \/  __ _ | |_  ___  ___      ___  _  _ __ ___   _   _ | |  __ _ | |_  ___   _ __  
| |     / _ \  / _` || | / __|    | | __  / _` || __|/ _ \/ __|    / __|| || '_ ` _ \ | | | || | / _` || __|/ _ \ | '__| 
| |____| (_) || (_| || || (__     | |_\ \| (_| || |_|  __/\__ \    \__ \| || | | | | || |_| || || (_| || |_| (_) || |    
\_____/ \___/  \__, ||_| \___|     \____/ \__,_| \__|\___||___/    |___/|_||_| |_| |_| \__,_||_| \__,_| \__|\___/ |_|    
                __/ |                                                                                                    
               |___/                                                                            created by : Aayush                         
'''

print(banner)
 
print("\n")
# main loop start 

user = input("enter your name :")

while  True:

    #taking input and designing
    print("========================================")   
    a = int(input("            input a : "))
    print("========================================")   
    b = int(input("            input b : "))
    print("========================================")   
   

    def retakeinput(): #retake input
        return int(input("enter the value "))

    def check_num(num):#checknum
        if num == 1 or  num == 0 :
            return True
        else:
            return False 

    def recheck(a,b):#recheck
        while not check_num(a) :
            print("renter the value for a as 0 or 1 only")
            a = retakeinput()
        while not check_num(b) :
            print("renter the value for b as 0 or 1 only")
            b = retakeinput() 

    #first checking 
    if not check_num(a):
        print("Invalid input for a.")
    if not check_num(b):
        print("Invalid input for b.")

    #starting next check  

    recheck(a,b)

    # gates functions

    def andgate(): #and ( y = a.b)
        out = a and b 
        return(bool(out))
    def orgate():#  or (y = a+b)
        out = a or b 
        return(bool(out))
    def nandgate(): #nand (y inve and)
        return not (a and b )    
    def norgate():# nor ( y = inv(a+b))
        return not (a + b )
    def xorgate():# xor (y = (a . binv )+ (ainv . b )
        return not (a == b )
    def xnorgate():# xnor (y = (a.b) +(iva + invb))
        return not (a != b)

    #displaying the gate options and then prompoting user to select

    list = [
        "AND-gate",
        "OR-gate",
        "NAND-gate",
        "NOR-gate",
        "XOR-gate",
        "XNOR-gate",
    ]

    while True :

        print("\n"," avilable LOGIC gates ","\n")    
        for i in range (0,len(list)):
            print(f"{i + 1}.{list[i]}")
        print("\n")

        choice = int(input("enter your choice to perfornm the binary operation : "))

        # print(list[choice - 1  ])

        if  choice == 1:
            print(f"the operation of AND GATE  with the two inputs {a} and {b} is {andgate()}")
            

        elif choice == 2:
            print(f"the operation of  OR GATE  with the two inputs {a} and {b} is {orgate()}")

        elif choice == 3:
            print(f"the operation of NAND GATE  with the two inputs {a} and {b} is {nandgate()}")

        elif choice == 4:
            print(f"the operation of NOR GATE  with the two inputs {a} and {b} is {norgate()}")

        elif choice == 5:
            print(f"the operation of XOR GATE  with the two inputs {a} and {b} is {xorgate()}")

        elif choice == 6:
            print(f"the operation of XNOR GATE  with the two inputs {a} and {b} is {xnorgate()}") 
            
        else :
            print("the choice you have entered is in correct please re-enter your choice .")
            choice = retakeinput()
        print("========================================")   
        try_another_gate = input("Do you want to try another gate? (yes/no): ")
        if try_another_gate.lower() != "yes":
            print(f"lets start again {user}" , end = " ")
            break
        print("========================================")   

    rerun = input("to try another boolean operation with diffrent values  , input yes  and to exit the code  enter no  (yes/no): ")
    if rerun.lower() != "yes":
            print("========================================")   
            print(f"see you again ,{user}")
            break
    print("========================================")   