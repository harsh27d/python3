number_list = input("Enter a list of numbers separated by spaces: ").split() #It will take input and split it
number_list = [int(num) for num in number_list] #Convert each element to an integer
number_list.insert(3,8) #Insert 8 at index 3
number_list.insert(4,9) #Insert 9 at index 4
number_list.append("pythoon") #Append "pythoon" to the end

part1 = number_list[:5] #Get the first 5 elements
part2 = number_list[5:] #Get the elements from index 5 to the end
print("Part 1:", part1)
print("Part 2:", part2)
