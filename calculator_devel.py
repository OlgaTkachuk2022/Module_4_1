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


def calc(num_1, num_2, choice):
   if choice == "+" :
    print(num_1, "+" , num_2, "=", add(num_1,num_2))
    logging.info(f"num_1 = {num_1},num_2 = {num_2},choice = {choice}")
    result = num_1 + num_2 

   elif choice == "-": 
     print(num_1, " - ", num_2, " = ", subtract(num_1, num_2))
     logging.info(f"num_1 = {num_1},num_2 = {num_2},choice = {choice}")
     result = num_1 - num_2

   elif choice == "*":   
     print(num_1, " * ", num_2, " = ", multiply(num_1, num_2)) 
     logging.info(f"num_1 = {num_1},num_2 = {num_2},choice = {choice}")  
     result = num_1 * num_2

   elif choice == '/': 
      try : 
          print(num_1, " / ", num_2, " = ", divide(num_1, num_2)) 
      except ZeroDivisionError :
         print("На нуль ділити не можна!")
      logging.info(f"num_1 = {num_1},num_2 = {num_2},,choice = {choice}")
      result = num_1 / num_2
     
   else:
    logging("This is an error") 

    return result 
logging.info(calc(num_1,num_2,choice))