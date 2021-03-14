print('Give me two numbers, and I will divide them. Enter q to quit')
while True:
    first_number=input("Enter first number: ")
    if first_number=='q':
        break;
    second_number=input("Enter second number: ")
    try:
        answer=int(first_number)/int(second_number)    
    except ZeroDivisionError:
        print('Can not divide by zero')    
    else:
        print(answer)
