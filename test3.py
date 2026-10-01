#Write a program to check the number is palindrome or not
num = int(input("Enter a number: "))
rev=0
n=num
while (num > 0):
 rev =rev * 10 + (num%10)
 n = n//10
 if rev == n:
  print("The number is palindrome")
 else:
  print("The number is not palindrome")
