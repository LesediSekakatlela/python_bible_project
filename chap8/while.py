#how loops work
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)

#using a while loop
number = 1

while number <= 10:
    print(number)
    number = number + 1
#prints out the number 11
print(number)



   
L = []

while len(L) < 5:
    new_name = input("Please add a new name: ").strip().capitalize()
    L.append(new_name)

print("Sorry list is full")
print(L)


