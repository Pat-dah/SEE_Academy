""" Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
Perform the operation based on the user's input and print the result.
Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15. """

# what is the 1st numner
first_num = int(input("Enter the ist number:  "))

# what is the second number

second_num = int(input("Enter the second number:" ))

#Add operation
sum = first_num + second_num

#diff#
diff = first_num -second_num

#multiplication 
prod = first_num * second_num

#Quotient
division = first_num / second_num 

print(f"Results of your two numbers:")
print(f"Sum: {sum}")  
print(f"Difference: {diff}")  
print(f"Product: {prod}")  
print(f"Quotient: {division}") 
