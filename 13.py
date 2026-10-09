#Accept the namee and check if its palandrome. 
pal = (input("Enter a string to check palandrome: "))

if pal == pal[::-1]:
    print(f"{pal} is palamdrome ")
else:
    print(f"{pal} is not palandrome")

 


