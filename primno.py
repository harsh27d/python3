int = int(input("Enter a number: "))
flag=0
for i in range (2, (int//2)+1):
  if (int % i == 0):
        flag = 1
        break

if flag == 1:
    print(int , "Is a prime number")
else:
    print(int , "Is not a prime number")
