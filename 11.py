#Print the tables of all odd number from 1 to 10
print("Table of odd numbers from 1 to 10")
for i in range(1, 11):
    if i % 2 != 0:
        print(f"Table of {i}:")
        for j in range(1, 11):
            print(f"{i}* {j} = {i*j}")
        print()


