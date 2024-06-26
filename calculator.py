values=[]
while  True:
     input_multi="*"
     input_add="+"
     input_div="/"
     input_sub="-"
#ask the user to input a value
     num1=input("enter a value :(or enter done)")

# to stop the 
     if num1 == "done" :
          break
# an expection that checks if the value entered is an integer (only accept integer)
     try:
        num1 = int(num1)
     except ValueError:
        print("Please enter a valid number.")
        continue
   
    #allows the user to input another value 
     values.append(num1)
     
     #checks the lenght of the value variable
     if len(values) < 2:
        print("Please enter another number for the operation.")
        continue
   
   
#input your operator
     operator=input("please enter your operator")
 #making sure it an operator that was entered    
     if operator not in [input_add, input_sub, input_div, input_multi]:
        print("Invalid operator.")
        continue
     num2=values[-2]
     
     if operator == input_add:
          total=num1 + num2
          print(total)
     elif operator == input_sub:
        total = num1 - num2
        print(total)
          
     elif operator == input_div:
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            total = num1 / num2
            print(total)
     elif operator == input_multi:
        total = num1 * num2
        print(total)
    
     else:
        print("Invalid operator.")
        print(num1)
        print(num2)
    
      #numofvalueentered=0
    
      #numofvalueentered+=1
     print(values)