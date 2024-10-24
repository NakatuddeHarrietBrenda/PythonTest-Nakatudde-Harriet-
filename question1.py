# Question 1(i)
# Write a Python program to find the distance between two coordinate points (x1, y1) and (x2, y2).
 
import math

X1 = int(input('\nEnter the value of X1:\t'))
Y1 = int(input('\nEnter the value of Y1:\t'))
X2 = int(input('\nEnter the value of X2:\t'))
Y2 = int(input('\nEnter the value of Y2:\t'))


distance = math.sqrt(X2-X1)**2*(Y2-Y1)**2
print(f'\nThe distance between the two coordinates is: {distance}\t')


# Question 1(ii)
# Write a Python program to find maximum between three numbers.

number_one = int(input('\nEnter the first number:\t'))
number_two = int(input('\nEnter the second number:\t'))
number_three = int(input('\nEnter the third number:\t'))

maximum_number = max(number_one, number_two, number_three)
print(f'\nThe maximum number of {number_one}, {number_two} and {number_three} is: {maximum_number}\t')


