# Question 3(i)
#  Write a Python program that prompts a user to enter numbers. The process will repeat until
#  the user enters 0. Finally, the program prints sum of the numbers entered by the user.


print('\n....Enter a number greater then 0....\t')

    

number_one = int(input('\nEnter the first number:\t'))
number_two = int(input('\Enter the second number:'))

sum_of_the_numbers = number_one + number_two
print(f'The sum of the numbers is: {sum_of_the_numbers}')






# Question 3(ii)
# Write a Python program to print all the numbers from 1 to 100 that are not divisible by 2
 
def numbers():
    number= input('Enter number:')

    if number>1 and number<100:
        print('not divisable by 2')
    else:
        print('not divisable by two')
numbers()

