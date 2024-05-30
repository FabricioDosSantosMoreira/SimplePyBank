from typing import Iterator, List

from conta.Conta import Conta


class ContaIterador(Iterator):

    __indice: int = 0

    def __init__(self, contas: List[Conta]) -> None:
        self._contas: List[Conta] = contas
        
    def __iter__(self):
        return self

    def __next__(self):
        try:

            conta = self.contas[self.indice]

            return f"""Agência: {conta.agencia}, 
                    Número: {conta.numero}, 
                    Titular: {conta.cliente.nome}, 
                    Saldo: R$ {conta.saldo:.2f}"""








        except IndexError:
            raise StopIteration

        finally:
            self.indice += 1

    @property
    def contas(self) -> List[Conta]:
        return self._contas

    @property
    def indice(self) -> int:
        return self.__indice
    
    @property
    @indice.setter
    def indice(self, valor) -> None:
        self.__index = valor