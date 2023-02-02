"""
Write a function called sum_of_even_numbers:
1. The function accepts a list of integers
2. It returns the sum of all even numbers in the list
3. It prints this number
"""
#For loop and if statement
def sum_of_even_numbers(num_list: list):
	sum_list = 0
	for number in num_list:
		if number % 2 == 0:
			sum_list += number
	return sum_list
	
num_list = [2, 3, 5, 7, 8, 10]	

sum_list = sum_of_even_numbers(num_list)
print(f'The sum of even numbers is {sum_list}')

#List comprehension
def sum_of_even_numbers_2(num_list: list):
	return sum([number for number in num_list if number % 2 == 0])

sum_list = sum_of_even_numbers_2(num_list)
print(f'The sum of even numbers is {sum_list}')
