from typing import List, Any
from wcwidth import wcswidth


from utils.string_utils import has_ascii

from utils.utils import categorizar_lista, garantir_paridade, atribuir_valores_distribuidos


from app.Configs import Configs


class Interface():

    def __init__(self, app) -> None:
        self.configs = Configs
        self.app = app
        

    def quit(self) -> None:
        self.app.is_running = False
        self.app.update()


    @staticmethod
    def warn(warning: str, *, warn_type: int) -> None:
        """
        Prints a warning message with a specified type.

        Args:
        warning (str): The warning message to be printed.
        warn_type (int): The type of warning. 
                            0 for ERROR, 
                            1 for MESSAGE, 
                            2 for WARNING, 
                            any other value for UNKNOWN.
        
        Returns: 
        None

        """
        w: str  # Initialize the warning string

        # Match the 'warn_type' to determine the appropriate warning label
        match warn_type:
            case 0:
                w = "ERROR"
            case 1:
                w = "MESSAGE"
            case 2:
                w = "WARNING"
            case _:
                w = "UNKNOWN"

        # Print the formatted warning message
        print(f'\n{w} - - - - -> {warning}')


    def menu(self) -> None:
        while True:

            print("\n")

            CABECALHO = ["OPÇÕES", "MENU"]
            CONTEUDO = categorizar_lista(["LOGIN / CADASTRO", 
                                           "ADMINISTRADORES", 
                                           "SAIR"])
            
            opcao: str = interface_interativa(
                            headers=CABECALHO,
                            contents=CONTEUDO,
                            msg=self.configs.msg_de_entrada,
                            min_str_size=TAMANHO_MINIMO_INTERFACE,
                            contents_str_pos=ALINHAMENTO_CONTEUDO,
                            header_str_pos=ALINHAMENTO_CABECALHO,
                        )
             
            match int(opcao):
                case 1:  # Entrar no menu de autenticação
                    self.menu_autenticacao()

                    continue    
                case 2:  # Entrar no menu do admin
                    self.menu_admin()

                    continue
                case 3:  # Sair do sistema
                    self.sair()
                          
    def menu_autenticacao(self) -> None:
        while True:
            
            print("\n")

            CABECALHO = ["OPÇÕES", "MENU DE AUTENTICAÇÃO"]
            CONTEUDO = categorizar_lista(["REALIZAR LOGIN",  
                                        "REALIZAR CADASTRO",  
                                        "VOLTAR",             
                                        "SAIR"])              

            opcao: str = select_list_option(
                            headers=CABECALHO,
                            contents=CONTEUDO,
                            msg=MENSAGEM_DE_ENTRADA,
                            min_str_size=TAMANHO_MINIMO_INTERFACE,
                            contents_str_pos=ALINHAMENTO_CONTEUDO,
                            header_str_pos=ALINHAMENTO_CABECALHO,
                        )
            
            match int(opcao):
                case 1:  # Entrar em um cliente
                    self.login_cliente()  

                    continue
                case 2:  # Cadastrar um cliente
                    self.cadastrar_cliente()  

                    continue
                case 3:  # Voltar ao menu
                    self.menu()

                    continue
                case 4:  # Sair do sistema
                    self.sair()  

    def cadastrar_cliente(self) -> None:
        while True:
            
            print("\n")

            CABECALHO = ["OPÇÕES", "MENU DE CADASTRO"]
            CONTEUDO = categorizar_lista(["CLIENTE PREMIUM", 
                                          "CLIENTE ESTUDANTE", 
                                          "CLIENTE PESSOA FÍSICA", 
                                          "CLIENTE PESSOA JURÍDICA", 
                                          "VOLTAR"])
                      
            opcao: str = select_list_option(
                            headers=CABECALHO,
                            contents=CONTEUDO,
                            msg=MENSAGEM_DE_ENTRADA,
                            min_str_size=TAMANHO_MINIMO_INTERFACE,
                            contents_str_pos=ALINHAMENTO_CONTEUDO,
                            header_str_pos=ALINHAMENTO_CABECALHO,
                        )
            
            match int(opcao):
                case 1:  # Cadastrar um cliente premium
                    from utils.cliente_utils import cadastrar_cliente_premium

                    cadastrar_cliente_premium(app=self.app)

                    continue
                case 2:  # Cadastrar um cliente estudante
                    from utils.cliente_utils import cadastrar_cliente_estudante

                    cadastrar_cliente_estudante(app=self.app)

                    continue
                case 3:  # Cadastrar um cliente pessoa física
                    from utils.cliente_utils import cadastrar_cliente_pessoa_fisica

                    cadastrar_cliente_pessoa_fisica(app=self.app)

                    continue
                case 4:  # Cadastrar um cliente pessoa jurídica
                    from utils.cliente_utils import cadastrar_cliente_pessoa_juridica

                    cadastrar_cliente_pessoa_juridica(app=self.app)
                    continue
                case 5:  # Voltar ao menu de autenticação
                    self.menu_autenticacao()

    def login_cliente(self) -> None:
        from utils.cliente_utils import login_cliente

        cliente = login_cliente(app=self.app)

        # O cliente conseguiu realizar o login?
        if cliente is not None:
            self.menu_cliente()
          
    def menu_cliente(self, cliente) -> None:

        pass
            





























   

    def menu_admin(self) -> None:
        while True:
            
            print("\n")
            raise NotImplementedError

   



    















def interface_interativa(
        cabecalho: List[str], 
        conteudo: List[Any], 
        pos_conteudo: List[str],
        pos_cabecalho: str,
        tamanho_min_string: int,
        msg: str,
        id_cabecalho_principal: int = 0, 
        ultima_col_como_alivio: bool = True
    ) -> str:

    string_da_borda: str = "+"
    string_dos_titulos: str = "|"

    # 


    # Create a list based on a size (len(headers)), Assigning integers representing a length
    # It can either distribute a value evenly or place a specific value at the end of the list
    str_sizes_list: list[int] = assign_distributed_value(
        size=len(headers),
        value=min_str_size,
        assign_value_at_end=last_col_as_min_str_size,
    )







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

        # If the value calculated in 'assign_distributed_value()' isn't enough, change to 'str_size'
        if str_sizes_list[i] < str_size:
            str_sizes_list[i] = str_size

    # Set 'str_sizes_list[-1]'
    if last_col_as_min_str_size:

        sizes_sum = sum(str_sizes_list) - str_sizes_list[-1]

        if str_sizes_list[-1] > max_content_len:
            str_sizes_list[-1] -= sizes_sum

        if str_sizes_list[-1] < max_content_len + len(headers[-1]):
            str_sizes_list[-1] = max_content_len + len(headers[-1]) - 8

    # Adjust the sizes in 'str_sizes_list' to ensure only even sizes, decrease by '1' if odd
    for i in range(len(str_sizes_list)):
        str_sizes_list[i] = ensure_value_parity(str_sizes_list[i], target_parity="even", decrease=True)

    # Build 'header_border_str' and 'headers_names_str'
    symbol_count_used: list = []
    for i in range(len(headers)):  # Iterate through each index of 'headers'

        # Build 'header_border_str'
        for symbol_count in range(
            str_sizes_list[i]
        ):  # Iterate through each index of 'str_sizes_list'

            if (symbol_count % 2) == 0:
                header_border_str += "-"  # Add "-" for even indices
            else:
                header_border_str += "="  # Add "=" for odd indices

            if str_sizes_list[i] - 2 == symbol_count:  # If it is the end of the column
                header_border_str += "+"  # add "+"

                symbol_count_used.append(
                    symbol_count
                )  # 'symbol_count_used' is used later when building 'formated_contents_str'
                break

        # Build 'headers_names_str', based on 'header_str_pos'
        if header_str_pos == "center":
            if len(headers[i]) % 2 != 0:
                header_names_str += (
                    f"{headers[i].upper().center(symbol_count + 1)}" + "|"
                )
            else:
                header_names_str += f"{headers[i].upper().center(symbol_count)}" + " |"

        elif header_str_pos == "right":
            header_names_str += f"{headers[i].upper().rjust(symbol_count - 2)}   " + "|"

        else:  # Default is 'left'
            header_names_str += f"   {headers[i].upper().ljust(symbol_count - 2)}" + "|"

    # Build 'formated_contents_str', based on 'contents_str_pos'
    formated_contents_str: str = ""
    for i in range(len(contents)):

        formated_contents_str += "|"

        for y in range(len(headers)):
            # If 'contents_str_pos' doesn't contain all positions, the last position is used
            try:
                str_pos = contents_str_pos[y]
            except IndexError:
                str_pos = contents_str_pos[-1]

            visual_width = 0

            if not contem_ascii(contents[i][y]):
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

    print(header_border_str)
    print(header_names_str)
    print(header_border_str)
    print(formated_contents_str, end="")
    print(header_border_str)

    while True:
        selection: int = read_int_input(msg=f"{msg}")

        if selection == -1:  # Stop
            return -1

        elif (
            len(contents) > (selection - 1) >= 0
        ):  # Return a str based on the selected content and 'main_header_id'
            return str(contents[selection - 1][main_header_id])

        else:
            warnings.warn(
                "\n\nWarning - - -> Selection wasn't valid. Please, Try again.\n",
                UserWarning,
                10,
            )


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