#Write a program to form a patter pyramid of 
#   * 
#  # # 
# / / /
pattern = int(input("Enter the number of rows: "))
for i in range(pattern):
    for j in range(pattern - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        if i % 3 == 0:
            print("*", end=" ")
        elif i % 3 == 1:
            print("#", end=" ")
        else:
            print("/", end=" ")
    print()