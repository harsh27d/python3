#Write a program to calculate the sum of digit of a number 
num = int(input("Enter a number: "))
sum=0
while (num > 0):
 sum =sum + (num%10)
 num = num//10
print(sum)