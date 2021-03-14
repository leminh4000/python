with open('pi_million_digits.txt') as file_object:
    lines=file_object.readlines()
pi_string=''

for line in lines:
    pi_string+=str(line.strip())
your_birth_date = input("enter your birth date yyddmm: ")
print(your_birth_date)

if pi_string.find(your_birth_date) == -1:
    print ("Your birth day is NOT in firt million pi digits")
else:
    print ("Your birth day is in firt million pi digits")    
    

