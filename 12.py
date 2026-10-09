#Create a heterogenous list of numbers and names. Split the list from highest number
h_list = [1,"abc" ,2 , "pqr" , 3 , "xyz"]
num  =[]
for i in h_list:
    if type(i) == int:
        num.append(i)   
print("Numbers in the list are:", num)
print("Highest number is:", max(num))
