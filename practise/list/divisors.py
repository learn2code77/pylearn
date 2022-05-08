''' Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number. '''

user_number = int(input("Enter a number "))

new_list = print([value for value in range(0, user_number+1) if value % 2 == 0])

print(" \n The same porgram using for loop \n")
anew_list = []
for value in range(0, user_number+1):
    if value % 2 == 0:
        anew_list.append(value)
print(anew_list)
