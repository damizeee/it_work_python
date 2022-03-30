print("                            BASIC AIRSPEXTA CALCULATOR")
print("                      + FOR ADD          ||          - FOR SUBTRACT  ")
print("                      * FOR MULTIPLY     ||          / FOR DIVIDE  ")

first_number = input("Enter your first input: ")
operator = input("Enter your operational Value: ")
second_number = input("Enter your second input: ")


if operator == "+":
      result = int(first_number) + int(second_number);
      print(result)
elif operator == "-":
      result = int(first_number) - int(second_number);
      print(result)
elif operator == "*":
      result = int(first_number) * int(second_number);
      print(result)
elif operator == "/":
      result = int(first_number) / int(second_number);
      print(result)
else:
     print("result not Found")
 #    print("Try again")

