from src.app.Interface import Interface
from src.classes.cliente.Cliente import Cliente
from src.classes.cartao.Cartao import Cartao
from src.classes.conta.Conta import Conta


from typing import List


class Main():

    def __init__(self) -> None:
        self.is_running: bool = True
        
        # TODO: Implementar carregamento via DB
        self._clientes: List[Cliente] = []
        self._cartoes: List[Cartao] = []
        self._contas: List[Conta] = []

        self.interface = Interface(self)


    def start(self) -> None:

        while self.is_running:
            self.interface.menu()

        quit('\nPyBank Fechado!')


    def update(self) -> None:
        self.start()
    
    @property
    def clientes(self) -> List[Cliente]:
        return self._clientes
    
    @property
    def cartoes(self) -> List[Cartao]:
        return self._cartoes
    
    @property
    def contas(self) -> List[Conta]:
        return self._contas


if __name__ == '__main__':
    app = Main()
    app.start()
