'''https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions. Make sure to ask the 
user to enter number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers
where the next number in the sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)'''

def fibFind(value):
    ''' A simple program to generate
    fibonacci nummber up to given value'''

    fab_series = [0,1]
    i = 0
    while fab_series[len(fab_series)-1] <= value:
        fab_series.append(fab_series[i] + fab_series[i+1])
        i += 1
    return fab_series



#number = int(input("Enter a valid number :- "))
#print(fibFind(number))
