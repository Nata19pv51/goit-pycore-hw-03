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


print(get_numbers_ticket(1, 50, 6))