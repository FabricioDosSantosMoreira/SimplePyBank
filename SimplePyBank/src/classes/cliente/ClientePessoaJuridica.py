from cliente.Cliente import Cliente
from datetime import date


# Extende a classe 'Cliente()'. Herança simples
class ClientePessoaJuridica(Cliente):

    def __init__(self, cep: str, cnpj: str, nome: str, data_nascimento: date) -> None:
        super().__init__(cep=cep, nome=nome, data_nascimento=data_nascimento)

        self._cnpj: str = cnpj

    @property
    def cnpj(self) -> str:
        return self._cnpj
