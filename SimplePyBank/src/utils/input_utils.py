from typing import Union


def read_str_input(*, msg: str) -> Union[str, int]:
    from app.Interface import Interface
    """
    Prompts the user for a string input, ensuring the input is valid and non-empty.

    Args:
        msg (str): The message to display when prompting the user for input.

    Returns: 
        Union[str, int]: The string value if it is valid. 
        -1 if the user interrupts the program or if any other error occurs.
        
    Raises:
        None. All exceptions are handled within the function.
    """
    while True:
        
        try:
            value = str(input(msg))

            if not value or value.isspace():
                raise ValueError

            return value

        except ValueError:
            Interface.warn('Invalid input. Please, try again.\n', warn_type=0)

        except KeyboardInterrupt:
            Interface.warn('Program interrupted by user.\n', warn_type=0)
            return -1
        
        except Exception as e:
            Interface.warn(f'An error occurred: {e}\n', warn_type=0)
            return -1


def read_int_input(*, msg: str) -> Union[str, int]:
    from app.Interface import Interface
    """
    Prompts the user for a integer input, ensuring the input is valid.

    Args:
        msg (str): The message to display when prompting the user for input.

    Returns: 
        Union[str, int]: The integer value if it is valid. 
        -1 if the user interrupts the program or if any other error occurs.
        
    Raises:
        None. All exceptions are handled within the function.
    """
    while True:

        try:
            value = int(input(msg))
            return value

        except ValueError:
            Interface.warn('Invalid input. Please, try again.\n', warn_type=0)

        except KeyboardInterrupt:
            Interface.warn('Program interrupted by user.\n', warn_type=0)
            return -1
        
        except Exception as e:
            Interface.warn(f'An error occurred: {e}\n', warn_type=0)
            return -1
