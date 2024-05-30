import pytz

from typing import List


class Configs():

    def __init__(self) -> None:

        # -=-=-=-=-=-=-=-=-=-=-=-=-= Interface =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        self.input_msg: str = "\n- - - - - - - -> INSERT AN OPTION: "

        # NOTE: The smallest size the interface should have. Greater values 
        # may not work, since 'min_interface_size' depends on the available 
        # terminal/screen size. 
        self.min_interface_size: int = 120

        # NOTE: The biggest size a string should have
        self.max_string_size: int = 90

        # NOTE: When a string is shortened a 'string_delimiter' is applied
        self.string_delimiter: str = '...'

        # NOTE: Available alignments: 'left', 'center', 'right'
        self.headers_alignment: str = ['left', 'left']
        self.content_alignment: List[str] = ['center', 'left']


        # -=-=-=-=-=-=-=-=-=-=-=-=-= Card =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        self.flag: str = "PyBank"
        self.flag_digit: int = 7
        self.card_digit_count: int = 19
        self.minimum_validity: int = 6 # 6 months
        self.branches: List[str] = ["0001", "0002", "0004"]
        self.payment_days: List[int] = [5, 15, 28]
        self.current_timezone: tuple = pytz.timezone('America/Sao_Paulo')
        self.interest_rate = 0.05 # 5% per month
