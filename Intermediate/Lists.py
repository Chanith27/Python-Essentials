numbers = [10,7,5,3,1]

numbers[2] = int(input("Input the number: "))

del numbers[4]

len(numbers)

print(numbers)

#Here we just get the length of the list
numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

#We add 4 for the end of the list
numbers.append(4)
print(len(numbers))
print(numbers)

#We insert the index, then number we want to add
numbers.insert(0, 222)
print(len(numbers))
print(numbers)

