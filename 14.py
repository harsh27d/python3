#calculate the digits of a number 
number = int(input("Enter digits: "))
sum = 0
while number>0:
    digit = number%10
    sum+=digit
    number//=10
print("Sum of digits is", sum)
