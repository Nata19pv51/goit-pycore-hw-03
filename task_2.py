import random

def get_numbers_ticket(min_num, max_num, quantity):
    
    # Create an empty set:
    random_nums_set = set()
    
    while len(random_nums_set) != quantity:
        # Use randrange() function to generate a number from min to max value, with step 1:
        random_num = random.randrange(min_num, max_num, 1)
        
        # Add random generated number to the set random_nums_set:
        random_nums_set.add(random_num)
        
    # Sort the random_nums_set
    random_nums_set = sorted(random_nums_set)
    
    return random_nums_set


def min_value_recurtion():
    try:
        min_value = int(input("Enter min value, >=1: "))
    except ValueError:
        # If user enter not integer, ValueError exception works. And we ask user to enter again
        print("The value should be integer.")
        return min_value_recurtion()
    else:
        # Check if min value corresponds to the conditions. If out of bounds, ask user enter again:
        if (min_value < 1) | (min_value > 998):
            print("The min value should be >= 1 or <= 998")
            return min_value_recurtion()
        else:
            return min_value
        

def max_value_recurtion(min_value):
    try:
        max_value = int(input("Enter max value, <=1000: "))
    except ValueError:
        # If user enter not integer, ValueError exception works. And we ask user to enter again
        print("The value should be integer.")
        return max_value_recurtion(min_value)
    else:
        # Check if max value corresponds to the conditions. If out of bounds, ask user enter again:
        if (max_value <= (min_value + 1)) | (max_value > 1000):
            print("The max value should be more than min value and <= 1000")
            return max_value_recurtion(min_value)
        else:
            return max_value
   
def quantity_value_recurtion(min_value, max_value):         
    try:
        quantity = int(input("Enter quantity, from min to max value: "))
    except ValueError:
        # If user enter not integer, ValueError exception works. And we ask user to enter again
        print("The value should be integer.")
        return quantity_value_recurtion(min_value, max_value)
    else:
        # Check if quantity corresponds to the conditions. If out of bounds, ask user enter again:
        difference = max_value - min_value
        if (quantity >= difference):
            print("The quantity should between min value and max value")
            return quantity_value_recurtion(min_value, max_value) 
        else:
            return quantity
  
min_value = min_value_recurtion()
max_value = max_value_recurtion(min_value)
quantity = quantity_value_recurtion(min_value, max_value)

# We call get_numbers_ticket to get unique random values using min and max values, quantity that user entered:  
random_nums_set = get_numbers_ticket(min_value, max_value, quantity)      
print(f"There are {quantity} unique random numbers: \n{random_nums_set}")
