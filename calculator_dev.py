import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")

def add(*args):
   return args[0] + args[1] 


def subtract(*args):   
   return args[0] - args[1] 


def multiply(*args):  
   return args[0] * args[1]


def divide(*args):  
   return args[0] / args[1] 

choice = input("Please enter choice(+/ -/ */ /): ")  
num_1 = int(input("Please enter the first number: "))   
num_2 = int(input("Please enter the second number: "))   


def calcul(num_1, num_2, choice):
   if choice == "+" :
    print(num_1, "+" , num_2, "=", add(num_1,num_2))
    result = num_1 + num_2
    return result 

   elif choice == "-": 
     print(num_1, " - ", num_2, " = ", subtract(num_1, num_2))
     logging.info("num_1 = {num_1},choice = {choice}")
     result = num_1 - num_2
     return result 

   elif choice == "*":   
     print(num_1, " * ", num_2, " = ", multiply(num_1, num_2)) 
     logging.info("num_1 = {num_1},choice = {choice}")  
     result = num_1 * num_2
     return result 

   elif choice == '/':   
     print(num_1, " / ", num_2, " = ", divide(num_1, num_2))  
     logging.info("num_2 = {0}{ division by zero}}")
     result = num_1 / num_2
     return result 
   else:
    print("This is an error") 

print (calcul(num_1 ,num_2 , choice))