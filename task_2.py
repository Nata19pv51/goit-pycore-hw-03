import random

def get_numbers_ticket(min_num, max_num, quantity):
    random_nums_set = set()
    if type(min_num) == int | type(max_num) == int | type(quantity) == int:
        if (min_num >= 1) & (min_num < 999):
            if (max_num > (min_num + 1)) & (max_num <= 1000):
                if quantity <= (max_num - min_num):
                    while len(random_nums_set) != quantity:
                        # Use randrange() function to generate a number from min to max value, with step 1:
                        random_num = random.randrange(min_num, max_num, 1)
        
                        # Add random generated number to the set random_nums_set:
                        random_nums_set.add(random_num)
        
                    # Sort the random_nums_set
                    random_nums_list = sorted(random_nums_set)
                    return random_nums_list
                
                else:
                    return None 
            else:
                return None 
        else:
            return None        
    else:
        return None
    
min_value = 2
max_value = 4
quantity = "0"

# We call get_numbers_ticket to get unique random values using min and max values, quantity that user entered:  
random_nums = get_numbers_ticket(min_value, max_value, quantity)      

if random_nums:
    print(f"There are {quantity} unique random numbers: \n{random_nums}")
else:
    print("Enter correct values")    