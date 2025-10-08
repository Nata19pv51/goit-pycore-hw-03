import random

def get_numbers_ticket(min_num, max_num, quantity):
    random_nums_set = set()
    
    while len(random_nums_set) != quantity:
        random_num = random.randrange(min_num, max_num, 1)
        random_nums_set.add(random_num)
    
    random_nums_set = sorted(random_nums_set)
    return random_nums_set


print(get_numbers_ticket(1, 50, 6))