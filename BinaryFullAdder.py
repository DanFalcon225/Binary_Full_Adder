import re #package to check special symbols within the string

#Bytes adder

#This program is a simulation of ALU opertation process
#The program enable user to add two bytes(8 bits) and produce the result
#Addition of each bit will go through to the adder, which includes specific logic gates

#Developer: Daniils Sokolovs
#Version: 12/05/2020

#---------------------------------------------------------------------------------------------------------------
print("Welcome to the Bytes adder simulator, which enables to add two bytes. The program simulates CPU operation process.\n")
print

#Validation of inputs#------------------------------------------------------------------------------------------- 

def validation(p,n):
    
    p1, n1 = len(p), len(n)    
    
    if p1 > 8 or n1 > 8: #inputs cannot be greater than 8 bits
        
        print ("The number(s) entered is greater than 8 bits. Also please check a format of input.\n")
        
        while choice:
    
            choice()
            
    elif p.isdigit() == False or n.isdigit() == False: #Function will not accepted any inputs except of digits

        print ("Invalid input! Some of the inputs are missing or data has been inputted in incorrect format.\n")

        while choice:
    
            choice()
            
    elif p.isdigit() == True and n.isdigit() == True: #Even if inputs are digis they must be in format of binary - (0,1)

        validation_string(p)
        
        validation_string(n)
            
    else:
        
        pass
    
        
#Extra validation for inputs#-----------------------------------------------------------------------------------
#Function aim to check whether the input contains numbers (2 - 9) if so it will not let program to be executed

def validation_string(m):

    s = re.compile('[2,3,4,5,6,7,8,9]')#checking input string for the specified symbols

    if(s.search(m) == None):
        
        pass
    
    else:

        print("The input should be in binary format - '0,1' \n")

        while choice:
    
            choice()

    
#Atjust lenght#--------------------------------------------------------------------------------------------------
#Function adjusting the length of the input in case if one greater than other
        
def adjust_lenght(d1, d2):

    f2 = '0'
    
    h1, h2 = len(d1), len(d2)
    
    if h1 > h2:
        
        d2 = d2.rjust(h1, f2) #if 1st input longer than 2nd one, adjusting length of 2nd by adding'0'
        
    elif h2 > h1:
        
        d1 = d1.rjust(h2, f2) #if 2nd input longer than 1st one, adjusting length of 2nd by adding '0'
        
    return (d1, d2)


#Input variables#----------------------------------------------------------------------------------------------

def get_input():

    print('')
    
    a1 = input("1st binary number: ")
    
    b1 = input("2nd binary number: ")
    
    print('')

    validation(a1,b1)

    return adjust_lenght(a1,b1)

        
    
#Function for AND gate#-----------------------------------------------------------------------------------------

def AND_operation(a,b):
    if a== 1 and b== 1:
        return 1
    else:
        return 0

#Function for OR gate#-------------------------------------------------------------------------------------------

def OR_operation(a,b):
    if a== 0 and b== 0:
        return 0
    else:
        return 1
        
#Function for XOR gate#------------------------------------------------------------------------------------------
        
def XOR_operation(a,b):
    if a== 0 and b== 0:
        return 0
    elif a== 1 and b== 1:
        return 0
    else:
        return 1

#Half added function#--------------------------------------------------------------------------------------------
#Adding two inputs to get sum and carry

def half_adder(a,b):

    a2 = XOR_operation(a,b)#gives sum
    
    b2 = AND_operation(a,b)#gives carry

    return (a2,b2)
    
    
#Full adder function#---------------------------------------------------------------------------------------------

def full_adder(a,b,cin = 0): #cin - stands for carry in

    sumA, cin1 = half_adder(a,b)
    
    sumB, cin2 = half_adder(sumA, cin)

    return(sumB, OR_operation(cin1,cin2))


#Binary string adder fuction#--------------------------------------------------------------------------------------

def binary_adder(a1,b1):
    
    result = ''
    cinG = 0

    for i in range (len(a1)-1,-1,-1): #iterating over the list in reverse direction
        
        sumG, cinG = full_adder(int(a1[i]), int(b1[i]), cinG)
        
        result = result + str(sumG)
        
    result = result + str (cinG)


    return result[::-1]# returning value in reverse order

#Main function#--------------------------------------------------------------------------------------------------
#Calls relevant functions to process binary addition

def main():
    
    a1,b1 = get_input()#getting input values

    result = binary_adder(a1, b1)#call binary adder function
    
    print("1st binary number: ", a1,"\n", "Integer represention: ", int(a1, 2), "\n")
    
    print("2st binary number: ", b1,"\n", "Integer represention: ", int(b1, 2), "\n")
    
    print("Result of addition: ",result,"\n", "Integer represention: ", int(result, 2), "\n")


#Choice function#------------------------------------------------------------------------------------------------

#Enable user to choose action

def choice():
    
    m = str(input("Please input '1' for binary addition or 'e' for exit: \n"))
    
    if m == str(1):
        main()
    elif m == 'e':
        exit()
    else:
        print ("Your choice has not been defined, please try again \n")

#While loop is not part of the choice() function it is
#aim to call mentioned function infinite times until the moment user decided to exit
        
while choice: 
    
    choice() 
        
        
        

        







