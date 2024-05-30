from app.Configs import Configs
from utils.utils import categorize_list
from utils.interface_utils import display_interactive_interface


class Interface():

    def __init__(self, app) -> None:
        
        self.configs = Configs()
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

            HEADERS = ["OPTIONS", "MENU"]
            CONTENTS = categorize_list(["LOGIN / REGISTER", 
                                           "ADMINISTRATORS", 
                                           "QUIT"])
            
            option: str = display_interactive_interface(
                            contents_pos=self.configs.content_alignment,
                            headers_pos=self.configs.headers_alignment,
                            contents=CONTENTS,
                            headers=HEADERS,
                            input_msg=self.configs.input_msg,
                            min_str_size=self.configs.min_interface_size,
                        )
             
            match int(option):
                case 1:  # Enter authentication menu
                    self.authentication_menu()

                    continue    
                case 2:  # Enter admin menu
                    self.admin_menu()

                    continue
                case 3:  # Quit system
                    self.quit()
                          

    def authentication_menu(self) -> None:
        while True:
            
            print("\n")

            HEADERS = ["OPTIONS", "AUTHENTICATION MENU"]
            CONTENTS = categorize_list(["LOG-IN",  
                                        "REGISTER",  
                                        "GO BACK",             
                                        "QUIT"])              

            option: str = display_interactive_interface(
                            contents_pos=self.configs.content_alignment,
                            headers_pos=self.configs.headers_alignment,
                            contents=CONTENTS,
                            headers=HEADERS,
                            input_msg=self.configs.input_msg,
                            min_str_size=self.configs.min_interface_size,
                        )
            
            match int(option):
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
                    self.quit()  

    def cadastrar_cliente(self) -> None:
        while True:
            
            print("\n")

            HEADERS = ["OPÇÕES", "MENU DE CADASTRO"]
            CONTENTS = categorize_list(["CLIENTE PREMIUM", 
                                          "CLIENTE ESTUDANTE", 
                                          "CLIENTE PESSOA FÍSICA", 
                                          "CLIENTE PESSOA JURÍDICA", 
                                          "VOLTAR"])
                      
            option: str = display_interactive_interface(
                            contents_pos=self.configs.content_alignment,
                            headers_pos=self.configs.headers_alignment,
                            contents=CONTENTS,
                            headers=HEADERS,
                            input_msg=self.configs.input_msg,
                            min_str_size=self.configs.min_interface_size,
                        )
            

            match int(option):
                case 1:  # Cadastrar um cliente premium
                    raise Exception
                    from utils.cliente_utils import cadastrar_cliente_premium

                    cadastrar_cliente_premium(app=self.app)

                    continue
                case 2:  # Cadastrar um cliente estudante
                    raise Exception
                    from utils.cliente_utils import cadastrar_cliente_estudante

                    cadastrar_cliente_estudante(app=self.app)

                    continue
                case 3:  # Cadastrar um cliente pessoa física
                    raise Exception
                    from utils.cliente_utils import cadastrar_cliente_pessoa_fisica

                    cadastrar_cliente_pessoa_fisica(app=self.app)

                    continue
                case 4:  # Cadastrar um cliente pessoa jurídica
                    raise Exception
                    from utils.cliente_utils import cadastrar_cliente_pessoa_juridica

                    cadastrar_cliente_pessoa_juridica(app=self.app)
                    continue
                case 5:  # Voltar ao menu de autenticação
                    self.authentication_menu()


    def login_cliente(self) -> None:
        raise Exception
        from utils.cliente_utils import login_cliente

        cliente = login_cliente(app=self.app)

        # O cliente conseguiu realizar o login?
        if cliente is not None:
            self.menu_cliente()
          
    def menu_cliente(self, cliente) -> None:

        pass
            





























   

    def admin_menu(self) -> None:
        while True:
            
            print("\n")
            raise NotImplementedError

   



    







