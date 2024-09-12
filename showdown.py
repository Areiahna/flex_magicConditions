#Task1 : Identify the Greatest 
    # Write a Python program that asks the user to enter three numbers. Your code should then identify and print out the largest number among the three.

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Last one, I promise!: "))

print("=" * 30)

largest_num =0
if (num1 > num2) and (num1 > num3):
    largest_num = num1
    print("The largest number is", largest_num)
elif (num2 > num1) and (num2 > num3):
    largest_num = num2
    print("The largest number is", largest_num)
elif (num3 > num1) and (num3 > num2):
    largest_num = num3
    print("The largest number is", largest_num)
else:
    print("Duplicate numbers??")


# largest = max(num1, num2, num3)    
# print("The largest number is:", largest)

#==============================================================

#Task2: Identify the Smallest
    # Improve upon your code from Task 1 to also determine the smallest number among the three and print it out.


if num1 != largest_num and (num1 < num2 and num1 < num3) :
    print ("The smallest number is:", num1)
elif num2 != largest_num and (num2< num1 and num2< num3):
    print("The smallest number is:", num2)
elif num3 != largest_num and (num3 < num1 and num3 < num2):
    print("The smallest number is:", num3)
else: 
    print("Duplicate numbers??")


# smallest = min(num1,num2,num3)
# print("The smallest number is:", smallest)

