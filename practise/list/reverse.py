# given a list reverse the contents
user_input = input("Enter a comma separated list \n")
a_list = user_input.split(",")
print(a_list)

count = len(a_list)

i = 1
reverse_list = []

while count >= i:
    for item in a_list:
        reverse_list.append(a_list[count - i])
        i += 1

print("Your reversed list is ", reverse_list)

##########################################################
print("\nThe same function using just a reverse method")

a_list.reverse()

print("Your reversed list is ", a_list)




