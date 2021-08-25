kod = input("Select Basic or Power Calculator (B/P): ")
kod = kod.upper()
if kod == "B":
  print("Welcome to Basic Calculator")
  num1 = float(input("Enter your first number: "))
  op = input("Enter your Operator [+,-,÷,*] ")
  num2 = float(input("Enter your third number: "))
  # code by Harish Rao
  if op == "+":
    print(num1 + num2)
  elif op == "-":
      print(num1 - num2)
  elif op == "÷":
        print(num1 / num2)
  elif op == "*":
        print(num1 * num2)
  else:
    print("lavdalo basha rasarandi..jugal kompa lo padestha")
          
          
elif kod == "P":
  base = float(input("Enter Your Base Number "))
  exp = float(input("Enter Your Exponent "))
  result = base ** exp
  
  print("Answer --> " + str(result))
  
else:
  print("lavdalo basha rasarandi..jugal kompa lo padestha")