from cliente.Cliente import Cliente
from datetime import date


# Extende a classe 'Cliente()'. Herança simples
class ClienteEstudante(Cliente):

    def __init__(self, cep: str, carteira_estudante: str, nome: str, data_nascimento: date) -> None:
        super().__init__(cep=cep, nome=nome, data_nascimento=data_nascimento)

        self._carteira_estudante: str = carteira_estudante
        
    @property
    def carteira_estudante(self) -> str:
        return self._carteira_estudante
