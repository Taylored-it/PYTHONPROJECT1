def add(x,y):
    return(x+y)

def subtraction(x,y):
    return(x-y)

def division(x,y):
    return(x//y)

def multiplecation(x,y):
    return(x*y)

num1=eval(input("enter the first number->"))
num2=eval(input("enter the second number->"))
num2=eval(input("enter the third number->"))
num2=eval(input("enter the fourth number->"))

print("please choose an operator->")
print("1.add operator")
print("2.subtraction operator")
print("3.division operator")
print("4.multiplecation operator")
print("5.exit")

while(True):
    choice=int(input("1,2,3,4,5"))
    if choice in (1,2,3,4,5):
        if choice==1:
            print("enter your first num",num1,"enter your second num",num2,add(num1,num2))
        elif choice==2:
            print("enter your first num",num1,"enter your second num",num2,subtraction(num1,num2))
        elif choice==3:
            print("enter your first num",num1,"enter your second num",num2,division(num1,num2))
        elif choice==4:
            print("enter your first num",num1,"enter your second num",num2,multiplecation(num1,num2))
        elif choice==5:
            print("thankyou :)")
            exit()

else:
    print("invalid number ntered please try again")





