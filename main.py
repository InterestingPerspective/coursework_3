from utils.load_operations import load_operations
from utils.sort_operations import sort_operations
from utils.get_last_5_operations import get_last_5_operations
from utils.date_converter import convert_date
from utils.mask_numbers import mask_numbers


operations = load_operations("operations.json")
sorted_operations = sort_operations(operations)
last_5_operations = get_last_5_operations(sorted_operations)

for operation in last_5_operations:
    print(f"""{convert_date(operation)} {operation['description']}
{mask_numbers(operation)}
{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n""")
