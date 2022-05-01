# given a list reverse the contents
user_input = input("Enter a list \n")
a_list = user_input.split()
print(a_list)

if isinstance(a_list, list):
    reverse_list = a_list[-1:]
    print("Here is the reverse list" , reverse_list)
else:
    print("You need to enter a correct list")

