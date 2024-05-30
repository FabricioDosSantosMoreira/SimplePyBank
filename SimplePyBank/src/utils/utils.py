from typing import Any


def categorize_list(list_to_categorize: list[Any]) -> list[list[Any]]:
    categorized_list: list[list[Any]] = []

    for i in range(len(list_to_categorize)):
        categorized_list.append([str(i + 1), list_to_categorize[i]])

    return categorized_list


def ensure_value_parity(value: int, *, target_parity: str = None, decrease: bool = False) -> int:
    current_parity = "even" if value % 2 == 0 else "odd"

    if current_parity != target_parity:
        if decrease:
            return value - 1
        else:
            return value + 1

    return value  # 'value' already has the desired parity


def assign_distributed_list(value: int, size: int, assign_at_end: bool = False) -> list[int]:
    
    # If 'value' is to be placed at the last index
    if assign_at_end:
        distributed_list = [0] * size  # Initialize 'distributed_list' with zeros
        distributed_list[-1] = value   # Assign the value to the last index

    # If 'value' is to be distributed evenly across the list
    else:
        distributed_value = value // size  # Calculate the value to be distributed
        distributed_list = [distributed_value] * size  # Assign list with 'distributed_value'

    return distributed_list 
