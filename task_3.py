import re

def normalize_phone(phone_number):
    phone_number = phone_number.strip()
    print(phone_number)
    # pattern_any_symbol  = r"^[(0-9_\+)^\s+]"
    pattern_any_symbol  = r"[^0-9\+]"
    formatted_phone = re.sub(pattern_any_symbol, "", phone_number)
    print(formatted_phone)
    
    pattern_begin_plus38 = r"^[^\+38]"
    match = re.search(pattern_begin_plus38, formatted_phone)
    if match:
        formatted_phone = "+38" + formatted_phone
    
    pattern_begin_plus3 = r"^[^\+3]"
    match = re.search(pattern_begin_plus3, formatted_phone)
    if match:
        formatted_phone = "+3" + formatted_phone
    
    pattern_begin_plus = r"^[^\+]"
    match = re.search(pattern_begin_plus, formatted_phone)
    if match:
        formatted_phone = "+" + formatted_phone    
    
    return formatted_phone

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
sanitized_numbers = []

for num in raw_numbers:
    formatted_phone = normalize_phone(num)
    sanitized_numbers.append(formatted_phone)
    
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)