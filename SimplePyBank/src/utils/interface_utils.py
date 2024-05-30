from utils.utils import ensure_value_parity, assign_distributed_list
from utils.input_utils import read_int_input
from utils.string_utils import has_ascii


from typing import List, Any
from wcwidth import wcswidth

def display_interactive_interface(
        contents_pos: List[str], 
        headers_pos: List[str], 
        contents: List[List[Any]], 
        headers: List[str], 
        input_msg: str, 
        min_str_size: int, 
        main_header_id: int = 0, 
        use_last_col: bool = True
    ) -> str:

    border_str: str = "+"
    header_title_str: str = "|"

    # Create a list based on a size (len(headers)), Assigning integers representing a length
    # It can either distribute a value evenly or place a specific value at the end of the list
    str_sizes_list: list[int] = assign_distributed_list(value=min_str_size, size=len(headers), assign_at_end=use_last_col)

    # Calculate each 'str_size' and change the 'str_sizes_list' if necessary.
    str_size: int
    for i in range(len(headers)):
        str_size = 8  # Default size of 8 characters

        # Get the maximum length of a content in contents.
        max_content_len = max(len(content[i]) for content in contents)

        # Sum the larger value to 'str_size'
        if max_content_len > len(headers[i]):
            str_size += max_content_len
        else:
            str_size += len(headers[i])

        # If the value calculated in 'assign_distributed_list' isn't enough, change to 'str_size'
        if str_sizes_list[i] < str_size:
            str_sizes_list[i] = str_size


    if use_last_col:
        sizes_sum = sum(str_sizes_list) - str_sizes_list[-1]

        if str_sizes_list[-1] > max_content_len:
            str_sizes_list[-1] -= sizes_sum

        if str_sizes_list[-1] < max_content_len + len(headers[-1]):
            str_sizes_list[-1] = max_content_len + len(headers[-1]) - 8


    # Adjust the sizes in 'str_sizes_list' to ensure only even sizes, decrease by '1' if odd
    for i in range(len(str_sizes_list)):
        str_sizes_list[i] = ensure_value_parity(str_sizes_list[i], target_parity="even", decrease=True)


    symbol_count_used: list = []
    for i in range(len(headers)): 

        # Build 'border_str'
        for symbol_count in range(str_sizes_list[i]): 

            if (symbol_count % 2) == 0:
                border_str += "-"  # Add "-" for even indices
            else:
                border_str += "="  # Add "=" for odd indices

            if str_sizes_list[i] - 2 == symbol_count: 
                border_str += "+"  # add "+" if it is the end of the column

                # 'symbol_count_used' is used later when building 'formated_contents_str'
                symbol_count_used.append(symbol_count)  
                break


    # Build 'header_title_str', based on 'headers_pos'
    for i in range(len(headers)):

        if headers_pos[i] == 'center':
            if len(headers[i]) % 2 != 0:
                header_title_str += (f"{headers[i].upper().center(symbol_count_used[i] + 1)}" + "|")
            else:
                header_title_str += f"{headers[i].upper().center(symbol_count_used[i])}" + " |"

        elif headers_pos[i] == 'right':
            header_title_str += f"{headers[i].upper().rjust(symbol_count_used[i] - 2)}   " + "|"

        else:  # Default is 'left'
            header_title_str += f"   {headers[i].upper().ljust(symbol_count_used[i] - 2)}" + "|"
        


    # Build 'formated_contents_str', based on 'contents_pos'
    formated_contents_str: str = ""
    for i in range(len(contents)):

        formated_contents_str += "|"

        for y in range(len(headers)):
            # If 'contents_str_pos' doesn't contain all positions, the last position is used
            try:
                str_pos = contents_pos[y]
            except IndexError:
                str_pos = contents_pos[-1]

            visual_width = 0

            if not has_ascii(contents[i][y]):
            #if has_non_ascii(contents[i][y], CARACTERES_NON_ASCII_PERMITIDOS):

                visual_width = wcswidth(contents[i][y])

                if visual_width >= 1: # NOTE: ERA 0
                    div = visual_width // len(
                        contents[i][y]
                    )  # How much spaces a non-ascii char uses when printing? 2,3??? etc
                    visual_width = (
                        visual_width // div
                    )  # So divide by how much space ocupy to get the true len

            # FIXME: you dont need to check if content_length is odd, just do len(str(contents[i][y]))
            if str_pos == "center":
                content_length = len(contents[i][y])
                if content_length % 2 != 0:
                    content_length += 1

                formated_contents_str += (
                    f"{contents[i][y].title().center(symbol_count_used[y] + 1 - visual_width)}"
                    + "|".rjust(content_length - symbol_count_used[y])
                )

            elif str_pos == "right":
                formated_contents_str += (
                    f"{contents[i][y].title().rjust(symbol_count_used[y] - 2 - visual_width)}   "
                    + "|"
                )

            else:  # Default is 'left'
                formated_contents_str += (
                    f"   {contents[i][y].title().ljust(symbol_count_used[y] - 2 - visual_width)}"
                    + "|"
                )

        formated_contents_str += "\n"

    print(border_str)
    print(header_title_str)
    print(border_str)
    print(formated_contents_str, end="")
    print(border_str)

    while True:
        selection: int = read_int_input(msg=f"{input_msg}")

        if selection == -1:  # Stop
            return -1

        elif (
            len(contents) > (selection - 1) >= 0
        ):  # Return a str based on the selected content and 'main_header_id'
            return str(contents[selection - 1][main_header_id])

        else:
            print("Warning - - -> Selection wasn't valid. Please, Try again.\n")





def show_msg_with_border(msg: str, size: int = 0):

    # Adjust size if it's less than the minimum required for the border and message
    size = max(len(msg) + 6, size)

    border_str: str = "+"

    if size % 2 != 0:
        remaining = 3
    else:
        remaining = 4

    # Build 'border_str'
    for symbol in range(size):  # Iterate through each index of 'str_sizes_list'

        if (symbol % 2) == 0:
            border_str += "-"  # Add "-" for even indices
        else:
            border_str += "="  # Add "=" for odd indices

        if size - remaining == symbol:  # If it is the end of the column
            border_str += "+"  # add "+"
            break

    print(border_str)
    print(f"|   {msg.ljust(size - remaining - 2)}" + "|")