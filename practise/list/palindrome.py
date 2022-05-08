# palindrome
'''Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that
 reads the same forwards and backwards.) '''

user_word = input("Enter a word ")
reverse_word = user_word[::-1]

if user_word == reverse_word:
    print(f"The word {user_word} is palindrome")
else:
    print(f"The word {user_word} is NOT palindrome")




