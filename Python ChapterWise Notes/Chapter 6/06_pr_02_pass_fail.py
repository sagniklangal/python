num1 = int(input("Enter the marks in math\n"))
num2 = int(input("Enter the marks in science\n"))
num3 = int(input("Enter the marks in humanities\n"))
num4 = (num1 + num2+ num3)/3
if(num4>=40 and num1>=33 and num2>=33 and num3>=33):
    print("Pass")
else:
    print("fail")