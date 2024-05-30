from cliente.Cliente import Cliente
from datetime import date


# Extende a classe 'Cliente()'. Herança simples
class ClientePessoaFisica(Cliente): 

    def __init__(self, cep: str, cpf: str, nome: str, data_nascimento: date) -> None:
        super().__init__(cep=cep, nome=nome, data_nascimento=data_nascimento)

        self._cpf: str = cpf

    @property
    def cpf(self) -> str:
        return self._cpf
