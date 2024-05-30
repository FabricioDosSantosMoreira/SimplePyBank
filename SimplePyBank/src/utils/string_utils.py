from typing import List


def reduce_str_length(
        string: str, 
        *, length: int = 30, 
        delimiter: str = "", 
        end_cut: bool = True,
        ) -> str:

    # Is length greater or equal to the string length? If so return the string.
    if length >= len(string):  
        return string

    # Is 'end_cut' True? If so return a string with an end cut
    if end_cut:  
        return string[0:length] + delimiter
    
    # Else return a string with a start cut
    else:
        return delimiter + string[len(string) - length:len(string)]


def reduce_list_of_str_length(
        list_of_strings: List[str],
        *,
        length: int = 30,
        delimiter: str = "",
        end_cut: bool = True,
        ) -> list[str]:

    for i, string in enumerate(list_of_strings):
        list_of_strings[i] = reduce_str_length(string, length=length, delimiter=delimiter, end_cut=end_cut)

    return list_of_strings


def has_ascii(string: str) -> bool:
    """
    Check if a string contains only ASCII characters.

    Args:
        string (str): The input string to be checked.

    Returns:
        bool: True if all characters in the string are ASCII, False otherwise.
    """
    for char in string:
        if ord(char) > 127:
            return False
        
    return True